<template>
  <div class="singer-detail card">
    <h1>가수 이름</h1>
    <img src="@/assets/singer.jpg" alt="singer" style="width: 200px; border-radius: 50%;">
    <p>가수 소개글</p>
    <SingerAlbum/>
    <SingerAlbum/>
  </div>
</template>

<script setup>
import SingerAlbum from './SingerAlbum.vue';
</script>

<style scoped>
.singer-detail {
  text-align: center;
  padding: 10px;
  border: 1px solid #000;
}

.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
}
</style>