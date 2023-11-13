<template>
  <div>
    <header class="header">
      <div class="wrapper">
        <nav class="nav">
          <RouterLink to="/" class="nav-link">Home</RouterLink>
          <RouterLink to="/products" class="nav-link">Products</RouterLink>
          <RouterLink to="/favorite" class="nav-link">
            Favorite 
            <span v-if="store.isFavoriteCount > 0" class="badge bg-primary">{{ store.isFavoriteCount }}</span>
          </RouterLink>
        </nav>
      </div>
    </header>

    <main class="main">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import {RouterLink, RouterView} from 'vue-router'
import { useProductStore  } from '@/stores/product';

const store = useProductStore()
// console.log(store.isFavoriteCount)

</script>

<style scoped>
.header {
  background-color: #333;
  color: white;
  padding: 10px 0;
}

.wrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.nav {
  display: flex;
  justify-content: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  margin: 0 15px;
  font-size: 18px;
}

.main {
  padding: 20px;
}
</style>