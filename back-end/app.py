from flask import Flask, request, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)  # 允许跨域请求

def scan_ports(target_ip, start_port, end_port):
    open_ports = {}
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports[port] = "Open"
        else:
            open_ports[port] = "Closed"
        sock.close()
    return open_ports

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    target_ip = data['target_ip']
    start_port = int(data['start_port'])
    end_port = int(data['end_port'])
    results = scan_ports(target_ip, start_port, end_port)
    return jsonify(results)

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    target_ip = data['target_ip']
    port = int(data['port'])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((target_ip, port))
    status = "Open" if result == 0 else "Closed"
    sock.close()
    return jsonify({port: status})

if __name__ == '__main__':
    app.run(debug=True)
