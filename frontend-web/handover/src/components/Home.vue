<template>
  <div>
    <h1>Hello</h1>
    <p>This is a basic screen layout.</p>
    <button @click="sayHello">Say Hello</button>
  </div>
</template>

<script>
export default {
  methods: {
    sayHello() {
      alert('Hello, Vue.js!');
    },
  },
};
</script>

<style>
body{
  background: #d9d9d9; /* not apply if you go from page-1 to page-2 */
}
</style>