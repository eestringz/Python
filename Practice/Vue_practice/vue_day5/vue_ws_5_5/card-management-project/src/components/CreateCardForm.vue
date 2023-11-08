<template>
  <div>
    <form>
      <!-- v-model 양방향 바인딩 필수 !! -->
      <label for="name" class="form-label">이름</label>
      <input type="text" id="name" class="form-input" v-model="name"> 
      <label for="title" class="form-label">직함</label>
      <input type="text" id="title" class="form-input" v-model="title">
      <!-- form 제출 시 새로 고침을 방지할 수 있도록 prevent 를 사용하여 바로 createCardEvent 함수가 실행되도록 함. -->
      <button class="form-button"
        @click.prevent="createCardEvent">명함 추가</button> 

    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'

const name = ref('')
const title = ref('')

const emit = defineEmits(['createCardEvent'])
const createCardEvent = function () {
  // cardInfo는 ref로 래핑하면 안된다! v-model이 변화를 자동 감지한다.
  const cardInfo = {
    name : name.value,
    title : title.value
  }

  emit('createCardEvent', cardInfo)
  name.value = ""
  title.value = ""

}
</script>

<style scoped>
.form-input {
  border: 1px solid #007acc;
  border-radius: 5px;
  width: 300px;
  height: 25px;
}


.form-label {
  font-size: 15px;
  font-weight: bold;
  margin: 5px 15px;
}

.form-button {
  background-color: white;
  border: 1px solid #007acc;
  border-radius: 5px;
  margin-left: 15px;
  padding: 10px;
  font-size: 15px;
  font-weight: bold;
  color: #007acc;
}
</style>