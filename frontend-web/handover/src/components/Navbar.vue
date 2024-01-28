<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="/">
        <img src="./icons/IconLogo.png" width="28" height="28" style="margin-right: 8px;">
        <text class="fw-bold" style="color: #109655;">Handover</text>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
      <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <div style="margin-left: 120px;" class="mt-3">
          <input
            style="padding-left: 15px; padding-top: 4px; padding-bottom: 4px; padding-end: 15px; border-radius:6px; border: 1px solid lightgray; width: 300px;"
            type="text"
            v-model="searchQuery"
            @input="performSearch"
            placeholder="Search..."
          />
          <img class="ms-2" style="width:24px" src="./icons/IconSearch2.png">
          <ul>
            <!-- Display search results here -->
            <li v-for="result in searchResults" :key="result.id">{{ result.name }}</li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.navbar.navbar-light{
  background-color: white!important;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.2);
  height: 60px;
}  
.container {
  margin-left:5px;
}
</style>
