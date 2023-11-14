<template>
  <div class="app-page">
    <RouterLink to="/">Main</RouterLink>
    <h1>pinia + router 연습하기</h1>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

</script>

<style scoped>
.app-page {
  margin: 10px;
}
</style>