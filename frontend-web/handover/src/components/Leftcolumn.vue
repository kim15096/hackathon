<template>
  <div class="left-column">
    <div class="sticky-top">
      <!-- Add your category and filter elements here -->
      <h4 class="fw-bold">Find your item</h4>
      <ul>
        <li>Category 1</li>
        <li>Category 2</li>
        <!-- Add more categories as needed -->
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "LeftColumn",
};
</script>

<style scoped>
.left-column {
  position: sticky;
  top: 0;
  height: 100vh;
  width: 300px;
  padding: 20px;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.2);
  border-radius: 0px 4px 4px 0px;
  background-color: #ffffff; /* Adjust the background color as needed */
}

/* Add any custom styles for your left column here */
</style>
