# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
import threading

app = Flask(__name__)
CORS(app)

scan_results = {}
scan_progress = {}

def scan_ports(url, start_port, end_port, task_id):
    open_ports = []
    total_ports = end_port - start_port + 1
    for i, port in enumerate(range(start_port, end_port + 1)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((url, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
        scan_progress[task_id] = int((i + 1) / total_ports * 100)
    scan_results[task_id] = open_ports
    scan_progress[task_id] = 100

@app.route('/api/scan', methods=['POST'])
def start_scan():
    data = request.json
    url = data.get('url')
    start_port = int(data.get('start_port'))
    end_port = int(data.get('end_port'))
    task_id = f"{url}_{start_port}_{end_port}"
    threading.Thread(target=scan_ports, args=(url, start_port, end_port, task_id)).start()
    return jsonify({"task_id": task_id})

@app.route('/api/progress/<task_id>', methods=['GET'])
def get_progress(task_id):
    progress = scan_progress.get(task_id, 0)
    return jsonify({"progress": progress})

@app.route('/api/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = scan_results.get(task_id, [])
    return jsonify({"open_ports": result})

if __name__ == '__main__':
    app.run(debug=True)
