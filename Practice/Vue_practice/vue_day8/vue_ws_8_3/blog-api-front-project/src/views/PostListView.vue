<template>
  <div>
    <h1>게시글 목록 페이지</h1>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePostStore } from '@/stores/posts'

const store = usePostStore()

onMounted(() => {
  store.getPostList()
})

</script>

<style scoped>

</style>