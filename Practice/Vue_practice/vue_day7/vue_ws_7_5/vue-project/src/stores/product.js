import { ref, computed } from 'vue'
import { defineStore  } from 'pinia'

export const useProductStore = defineStore('product', () => {
  // states
  const productList = ref([
    {
      name: '상품 1',
      imagePath: 'src/assets/product1.png',
      price: 10000,
      isFavorite: false
    },
    {
      name: '상품 2',
      imagePath: 'src/assets/product2.png',
      price: 20000,
      isFavorite: false
    },
    {
      name: '상품 3',
      imagePath: 'src/assets/product3.png',
      price: 30000,
      isFavorite: false
    },
    {
      name: '상품 4',
      imagePath: 'src/assets/product4.png',
      price: 40000,
      isFavorite: false
    }
  ])

  // actions
  const updateProduct = function (name) {
    productList.value = productList.value.map((product) => {
      if (product.name === name ) {
        product.isFavorite = !product.isFavorite
      }
     return product
    })
  }

  // getters
  const isFavoriteCount = computed(() => {
    return productList.value.filter((product) => product.isFavorite).length
  }) 

  const isFavoriteList = computed(() => {
    return productList.value.filter((product) => product.isFavorite)
  })


  return { productList, updateProduct, isFavoriteCount, isFavoriteList }
}, { persist : true })

// defineStore의 3번째 인자로 관련 객체 추가
// { persist : true }