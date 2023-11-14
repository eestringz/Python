<template>
    <div class="main-page">
        <h3>메인 페이지</h3>
        <MainPage
            v-for="balance in store.balances"
            :key="balance.name"
            :balance="balance"
        />
    </div>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';
import { useBalanceStore  } from '@/stores/balance';


const store = useBalanceStore()


</script>

<style scoped>
.main-page { 
    margin: 30px;
}
</style>