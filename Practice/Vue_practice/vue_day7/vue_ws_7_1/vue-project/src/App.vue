<template>
  <nav class="navbar navbar-expand-lg bg-dark border-bottom border-body" data-bs-theme="dark">
    <div class="container-fluid">
      <a class="navbar-brand">Shopping Mall</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <RouterLink to="/" class="nav-link">Home</RouterLink>
          <RouterLink to="/products" class="nav-link">Products</RouterLink>
          <RouterLink to="/favorite" class="nav-link">Favorite</RouterLink>
        </div>
      </div>
    </div>
  </nav>
  <RouterView />
</template>

<script setup>
import {RouterLink, RouterView} from 'vue-router'


</script>

<style scoped>

</style>