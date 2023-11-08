<template>
  <div class="child-page">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  child : Object
})

</script>

<style scoped>
.child-page {
  border: 1px solid #333;
  padding: 10px;
  margin-bottom: 10px;
}
</style>