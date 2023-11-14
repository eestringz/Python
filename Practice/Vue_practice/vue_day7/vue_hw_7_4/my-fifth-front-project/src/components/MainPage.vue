<template>
    <div>
        <p>이름 : {{ balance.name }}</p>
        <p>잔고 : {{ balance.balance }}</p>
        <RouterLink 
            :to="{name:'update', params:{name : balance.name}}" 
            type="button" 
            class="btn btn-primary">updateBalance</RouterLink>
        <hr>
    </div>
</template>

<script setup>
import {RouterLink} from 'vue-router'
defineProps({
    balance : Object,
})



</script>

<style scoped>

</style>