<template>
  <div class="product-card">
    <p class="product-name">{{ product.name }}</p>
    <img 
      :src="product.imagePath"
      :alt="product.name"
      width="250"
    >
    <p class="product-price">₩ {{ product.price }}</p>
    <p v-if="product.isFavorite" class="favorite-icon" role="img" style="color:red">🤍</p>
    <p v-else class="favorite-icon" role="img">🤍</p>
  </div>
</template>

<script setup>
defineProps({
  product : Object,
})

</script>

<style scoped>
.product-card {
  border: 1px solid #ccc;
  text-align: center;
  width: 300px;
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
  font-size: 24px;
  margin-top: 10px;
}
</style>