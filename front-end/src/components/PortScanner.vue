<template>
  <div>
    <h1>Port Scanner</h1>
    <div>
      <label for="url">URL:</label>
      <input v-model="url" id="url" type="text" />
    </div>
    <div>
      <label for="startPort">Start Port:</label>
      <input v-model.number="startPort" id="startPort" type="number" />
    </div>
    <div>
      <label for="endPort">End Port:</label>
      <input v-model.number="endPort" id="endPort" type="number" />
    </div>
    <button @click="startScan">Start Scan</button>
    
    <div v-if="progress >= 0">
      <progress :value="progress" max="100"></progress>
      <p>{{ progress }}% completed</p>
    </div>
    
    <div v-if="openPorts.length > 0">
      <h2>Open Ports:</h2>
      <table>
        <thead>
          <tr>
            <th>Port</th>
            <th>Protocol</th>
            <th>Status</th>
            <th>Service</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="port in openPorts" :key="port.port">
            <td>{{ port.port }}</td>
            <td>{{ port.protocol }}</td>
            <td>{{ port.status }}</td>
            <td>{{ port.service }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      url: '',
      startPort: null,
      endPort: null,
      taskId: null,
      progress: -1,
      openPorts: []
    };
  },
  methods: {
    async startScan() {
      this.progress = 0;
      this.openPorts = [];
      const response = await axios.post('http://127.0.0.1:5000/api/scan', {
        url: this.url,
        start_port: this.startPort,
        end_port: this.endPort
      });
      this.taskId = response.data.task_id;
      this.pollProgress();
    },
    async pollProgress() {
      const interval = setInterval(async () => {
        const response = await axios.get(`http://127.0.0.1:5000/api/progress/${this.taskId}`);
        this.progress = response.data.progress;
        if (this.progress === 100) {
          clearInterval(interval);
          this.getResult();
        }
      }, 1000);
    },
    async getResult() {
      const response = await axios.get(`http://127.0.0.1:5000/api/result/${this.taskId}`);
      this.openPorts = response.data.open_ports;
    }
  }
};
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
}

div {
  margin: 20px;
}

label {
  display: inline-block;
  width: 100px;
}

input {
  margin: 10px 0;
}

button {
  margin: 20px 0;
}

progress {
  width: 100%;
  height: 20px;
  margin: 20px 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

th, td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: center;
}

th {
  background-color: #f4f4f4;
}
</style>
