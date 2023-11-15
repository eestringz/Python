import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCategoryStore = defineStore('category', () => {
  
  const categories = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getCategoryList = function () {
    axios({
      method : 'get',
      url : `${API_URL}/api/v1/category/`
    })
      .then((res) => {
        // console.log(res.data)
        categories.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return {categories, API_URL, getCategoryList}


}, {persist: true})