<template>
  <div class="child-list">
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  child : Object,
})
</script>

<style scoped>
.child-list {
  background-color: white;
  border: 1px solid #ccc;
  margin: 30px;
  padding: 20px;
  text-align: center;
}

</style>