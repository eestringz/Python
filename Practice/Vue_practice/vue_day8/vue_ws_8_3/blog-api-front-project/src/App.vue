<template>
  <div class="wrapper">
    <nav>
      <RouterLink :to="{name : 'main'}">Home</RouterLink>
      <RouterLink :to="{name : 'posts'}">PostList</RouterLink>
    </nav>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>
.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

nav {
  display: flex;
  justify-content: center;
  background-color: #333;
  padding: 1px;
}

nav a {
  color: #fff;
  text-decoration: none;
  margin: 1rem;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}
</style>