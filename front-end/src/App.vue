<!-- src/App.vue -->
<template>
  <div id="app">
    <PortScanner />
  </div>
</template>

<script>
import PortScanner from './components/PortScanner.vue';

export default {
  name: 'App',
  components: {
    PortScanner
  }
};
</script>

<style>
/* 添加一些全局样式 */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
