import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const usePostStore = defineStore('post', () => {
  
  const posts = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getPostList = function () {
    axios({
      method : 'get',
      url : `${API_URL}/api/v1/posts/`
    })
      .then((res) => {
        // console.log(res.data)
        posts.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const detailPost = ref([])
  const getDetailPost = function (pk) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/posts/${pk}`
    })
    .then(res => detailPost.value = res.data)
    .catch(err => console.log(err))
  }


  
  const updatePost = function ({pk, category, title, content}) {
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
      data: {
        category,
        title,
        content
      }
    })
  }

  const router = useRouter()
  
  const deletePost = function (pk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
    })
    .then(res => router.push({name:'posts'}))
  }

  return {posts,API_URL, getPostList, detailPost, getDetailPost, updatePost, deletePost}


}, {persist: true})
