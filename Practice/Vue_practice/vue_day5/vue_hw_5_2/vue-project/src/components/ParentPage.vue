<template>
  <div class="parent-page">
    <h1>부모 페이지입니다.</h1>
    <ChildernPage 
      v-for="child in children" 
      :key="child.name" 
      :child="child"
    />
  </div>
</template>

<script setup>
import {ref} from 'vue'
import ChildernPage from '@/components/ChildrenPage.vue'


const children = ref([
  {
    name : '김하나',
    age : 30
  },
  {
    name : '김두리',
    age : 20
  },
  {
    name : '김서이',
    age : 10
  },
])

</script>

<style scoped>
.parent-page {
  border: 1px solid #333;
  padding: 10px;
  margin: 10px;
}
</style>