<template>
  <div class="app-navbar">
    <Navbar/>
  </div>
  <div>
    <div class="app-left-column mt-1" >
      <LeftColumn />
    </div>
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

.app-left-column {
  position: fixed;
  left: 0;
  top: 60px; /* Adjust the top position to match the Navbar height */
  width: 200px; /* Adjust the width as needed */
  z-index: 2; /* Ensure LeftColumn is above other content except Navbar */
}
</style>
