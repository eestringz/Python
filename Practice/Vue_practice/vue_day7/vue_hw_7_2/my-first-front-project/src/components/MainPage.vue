<template>
  <div>
    <h1 class="title">pinia 연습하기</h1>
    <ParentPage 
      v-for="family in store.familyInfo"
      :key="family.familyName"
      :family="family"
    />
  </div>
</template>

<script setup>
import ParentPage from '@/components/ParentPage.vue';
import { useFamilyStore  } from '@/stores/family';

const store = useFamilyStore()
console.log(store.familyInfo)


</script>

<style scoped>
.title {
  margin-left: 20px;
}
</style>