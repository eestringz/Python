<template>
  <div class="product-card">
    <p class="product-name">{{ product.name }}</p>
    <img 
      :src="product.imagePath"
      :alt="product.name"
      width="250"
    >
    <p class="product-price">₩ {{ product.price }}</p>
    <span @click="store.updateProduct(product.name)">
      <span v-if="product.isFavorite" class="favorite-icon" role="img" style="color:red">❤</span>
      <span v-else class="favorite-icon" role="img">🤍</span>
    </span>
</div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';

defineProps({
  product : Object,
})

const store = useProductStore()

</script>

<style scoped>
.product-card {
  border: 1px solid #ccc;
  text-align: center;
  width: 350px;
  padding: 20px;
  margin: 10px;
}

.product-name {
  font-size: 20px;
  margin-bottom: 10px;
}


.product-price {
  font-size: 18px;
  margin-bottom: 10px;
}

.favorite-icon {
  cursor: pointer;
  font-size: 20px;
  margin-top: 10px;
}
</style>