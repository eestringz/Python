<template>
  <div>
    <!-- <ul v-for="article in store.articles" :key="article.id">
      <li>제목 : {{ article.title }} -
        내용 : {{article.content}}</li>
    </ul> -->
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style lang="scss" scoped>

</style>