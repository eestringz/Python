<template>
  <div class="business-card-detail">
    <h3>이름 : {{ businessCard.name }}</h3>
    <p>직함 : {{ businessCard.title }}</p>
    <button @click="deleteCardEvent(businessCard)">명함 삭제</button>
  </div>
</template>

<script setup>
defineProps({
  businessCard : Object
})

const emit = defineEmits(['deleteCardEvent'])

const deleteCardEvent = function (targetCard) {
  emit('deleteCardEvent', targetCard)
}

</script>

<style scoped>
.business-card-detail {
  background-color: #f9f9f9;
  width: 40%;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
}

</style>