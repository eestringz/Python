<template>
  <div class="quiz-create">
    <h2>퀴즈 생성</h2>
    <form class="quiz-form" @submit.prevent="createQuiz">
      <label for="question" class="form-label">문제</label>
      <!-- required 속성을 사용하여 필수 입력값으로 설정하고 경고 표시 -->
      <textarea 
        id="question" 
        class="form-input" 
        maxlength="200" rows="5" 
        v-model="newquiz.question" 
        required> 
      </textarea>

      <label for="answer" class="form-label">답안</label>
      <input 
        type="text" 
        id="answer" 
        class="form-input" 
        v-model="newquiz.answer" 
        required>

      <button class="form-button">퀴즈 생성</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['createQuiz'])

const newquiz = ref({
  question : '',
  answer : ''
})

const createQuiz = function () {
  // 빈 내용의 퀴즈를 생성할 수 없다.
  if (newquiz.value.question && newquiz.value.answer) {
    emit('createQuiz', newquiz.value)
    newquiz.value.question = ''
    newquiz.value.answer = ''
  }
  }

</script>

<style scoped>
.quiz-create {
  background-color: #ccc ;
  max-width: 600px;
  margin: 0 auto;
  margin-top: 50px ;
  padding: 20px;
  border-radius: 10px;
  font-family: Arial, sans-serif;
}

.quiz-form {
  display: flex;
  flex-direction: column;
}

.form-label {        
  display: block;
  font-size: 15px;
  margin-top: 15px;
}

.form-input {
  width: calc(100% - 24px);
  /* textarea 요소의 크기를 조정할 수 없도록  resize : none; */
  resize: none; 
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 15px;
  margin-top: 8px;
}

.form-button {
  background-color: deepskyblue ;
  border: none;
  border-radius: 5px;
  margin-top: 15px;
  padding: 15px;
  color: white;
  cursor: pointer;
  font-size: 15px;
}


/* ':hover' 를 사용하여 요소가 마우스 커서 위로 이동할 때의 스타일 정의 */
.form-button:hover {
  background-color: dodgerblue ;
}

</style>