<template>
    <div class="left-column">
      <div class="sticky-top">
        <!-- Add your category and filter elements here -->
        <h4>Categories</h4>
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
    padding: 20px;
    background-color: #f8f9fa; /* Adjust the background color as needed */
    border-right: 1px solid #dee2e6; /* Add a border to separate it from the main content */
  }
  
  /* Add any custom styles for your left column here */
  </style>
  