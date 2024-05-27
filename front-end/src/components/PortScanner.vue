<template>
  <div class="port-scanner">
    <h1>Port Scanner</h1>
    <form @submit.prevent="scanPorts">
      <label for="target_ip">Target IP:</label>
      <input type="text" v-model="targetIp" required />

      <label for="start_port">Start Port:</label>
      <input type="number" v-model="startPort" required />

      <label for="end_port">End Port:</label>
      <input type="number" v-model="endPort" required />

      <button type="submit">Scan</button>
    </form>
    <div v-if="results">
      <h2>Scan Results</h2>
      <ul>
        <li v-for="(status, port) in results" :key="port">
          Port {{ port }}: {{ status }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      targetIp: '',
      startPort: '',
      endPort: '',
      results: null
    };
  },
  methods: {
    async scanPorts() {
      try {
        const response = await axios.post('/api/scan', {
          target_ip: this.targetIp,
          start_port: this.startPort,
          end_port: this.endPort
        });
        this.results = response.data;
      } catch (error) {
        console.error('Error scanning ports:', error);
      }
    }
  }
};
</script>

<style scoped>
.port-scanner {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

form {
  margin-bottom: 20px;
}

label {
  display: block;
  margin: 10px 0 5px;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

h2 {
  margin-top: 20px;
}
</style>
