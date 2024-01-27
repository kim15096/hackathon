<template>
  <div class="app-navbar">
    <Navbar/>
  </div>
  <router-view></router-view>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import LeftColumn from "./components/Leftcolumn.vue";

export default {
  components: {
    Navbar,
    LeftColumn,
  },
};
</script>

<style>
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body{
  font-family: "Montserrat", sans-serif;
  line-height: 1.6;
  color: #333;
}
</style>

<style scoped>
.app-navbar {
  position: fixed;
  left: 0;
  top: 0; /* To make it stick to the very left of the page */
  width: 100vw; /* Adjust the width as needed */
}
</style>
