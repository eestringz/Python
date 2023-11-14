import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

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
        // console.log(err)
      })
  }

  return {posts,API_URL, getPostList}


}, {persist: true})