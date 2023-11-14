import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
    const balances = ref([
        {
            name: '김하나',
            balance: 100000
        },
        {
            name: '김두리',
            balance: 10000
        },
        {
            name: '김서이',
            balance: 100
        },
    ])


    const getBalanceByName = function (name) {
        return balances.value.find((balance) => balance.name === name);
    }
    

    const updateBalance = function(name, amount) {
        const balance = this.getBalanceByName(name);
        if (balance) {
            balance.balance += amount;
        }
    }

    return { balances, getBalanceByName , updateBalance}

})