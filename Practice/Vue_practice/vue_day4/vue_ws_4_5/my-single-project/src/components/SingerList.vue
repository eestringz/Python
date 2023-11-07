<template>
  <div class="singer-list">
    <h1 >가수 목록</h1>
    <SingerDetail v-for="singer in singers" :key="singer.name"/>
  </div>
</template>

<script setup>
import SingerDetail from './singers/SingerDetail.vue';
import {ref} from 'vue'

const singers = ref([
  {name : 'adele'},
  {name : 'maroon5'},
  {name : 'Dua Lipa'}
])

</script>

<style scoped>
.singer-list {
  text-align: center;
  padding: 10px;
}

.singer-list h1 {
  color: orangered;
}
</style>