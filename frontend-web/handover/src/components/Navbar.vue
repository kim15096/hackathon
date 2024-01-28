<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="/">
        <img src="./icons/IconLogo.png" width="28" height="28" style="margin-right: 8px;">
        <text class="fw-bold">Handover</text>
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
        <ul class="navbar-nav ml-auto">
          <!-- Add your navbar links here -->
          <li class="nav-item">
            <a class="nav-link" href="/items">Items</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/Yumin">Yumin</a>
          </li>
          <!-- Add more links as needed -->
        </ul>
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
}  
.container {
  margin-left:15px;
}
</style>
