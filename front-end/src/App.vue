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

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
