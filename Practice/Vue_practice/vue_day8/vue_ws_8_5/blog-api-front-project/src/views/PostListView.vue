<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <RouterLink :to="{name : 'post'}">게시글 생성</RouterLink>
    <ul>
      <div
        v-for="post in store.posts"
        :key="post.id"
        :post="post"
        @click="goDetail(post.id)"
      >
        <p>{{ post.category.name }}</p>
        <h3><span>{{post.id}}번 글 |</span> {{ post.title }}</h3>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePostStore } from '@/stores/posts'
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router'

const store = usePostStore()
const router = useRouter()

onMounted(() => {
  store.getPostList()
})

const goDetail = function (pk) {
  console.log(pk)
  router.push( {name : "detail", params : {pk : pk} })
}

</script>

<style scoped>

</style>