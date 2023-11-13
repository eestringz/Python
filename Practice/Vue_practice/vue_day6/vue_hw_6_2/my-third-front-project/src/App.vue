<template>
  <div>
    <MainPage />
    <RouterLink to="/">Some</RouterLink> |
    <RouterLink to="/other">Other</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';
import {RouterLink, RouterView} from 'vue-router'


</script>

<style scoped>

</style>