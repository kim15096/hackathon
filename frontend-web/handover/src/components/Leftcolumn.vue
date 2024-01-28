<template>
  <div class="left-column">
    <div class="sticky-top">
      <!-- Add your category and filter elements here -->
      <h4 class="fw-bold"><img class="ms-3 me-3" src="./icons/IconSearch.png">Find your item</h4>
      <div class="mt-3" style="width: 100%; height: 1px; background: rgb(200, 200, 200)"></div>
      <div class="form-check form-switch ms-3 mt-4">
        <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
        <label class="form-check-label fw-bold" for="flexSwitchCheckDefault">Certified</label>
      </div>
      <div class="form-check form-switch ms-3 mt-2">
        <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
        <label class="form-check-label fw-bold" for="flexSwitchCheckDefault">Borrow available</label>
      </div>
      <h5 class="fw-bold mt-5"><img style="height: 30px;" class="ms-3 me-3" src="./icons/IconCategories.png">Categories</h5>
      <button class="btn btn-outline-primary ms-3 mt-3">Electronics</button>
      <button class="btn btn-outline-dark ms-3 mt-3">Clothing</button>
      <button class="btn btn-outline-dark ms-3 mt-3">Beauty</button>
      <button class="btn btn-outline-dark ms-3 mt-3">School Supplies</button>
      <button class="btn btn-outline-dark ms-3 mt-3">Accessories</button>
      <button class="btn btn-outline-dark ms-3 mt-3">Furniture</button>
      <div class="mt-5" style="width: 100%; height: 1px; background: rgb(228, 228, 228)"></div>
      <div class="mt-5"></div>
      <img class="mt-5" style="width: 150px;" src="./icons/IconHandOver.png">
      <p class="ms-4 mt-4 fw-normal" style="font-size: 14px; color:rgb(97, 97, 97)">Hand over and earn money!</p>
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
  width: 275px;
  padding: 20px 0 20px 0;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.2);
  border-radius: 0px 4px 4px 0px;
  background-color: #ffffff; /* Adjust the background color as needed */
}

/* Add any custom styles for your left column here */
</style>
