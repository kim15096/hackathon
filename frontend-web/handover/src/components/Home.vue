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
  