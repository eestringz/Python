<template>
    <div class="update-page">
        <h2>데이터 수정 페이지</h2>
        <p>이름 : {{ balance.name }}</p>
        <p>잔고 : {{ balance.balance }}</p>
        <button @click="increaseBalance">+</button>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import {useRoute} from 'vue-router'
import {useBalanceStore} from '@/stores/balance'

const route = useRoute()
const userName = ref(route.params.name)
// console.log(getName)

const store = useBalanceStore()

const balanceName = route.params.name;
const balanceStore = useBalanceStore();
const balance = balanceStore.getBalanceByName(balanceName);

const increaseBalance = () => {
  balanceStore.updateBalance(balanceName, 1000);
};


</script>

<style scoped>

</style>