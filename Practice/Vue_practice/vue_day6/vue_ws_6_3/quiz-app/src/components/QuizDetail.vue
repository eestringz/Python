<template>
  <div class="quiz-item">
    <h4 class="quiz-question">{{ quiz.pk }}번 문제. {{ quiz.question }}</h4>
    <label :for="'answer' + quiz.pk" class="answer-label">정답 입력</label>
    <input type="text" :id="'answer' + quiz.pk" class="answer-input">
  </div>
</template>

<script setup>
defineProps({
  quiz : Object
})

</script>

<style scoped>
.quiz-item {
  background-color: #f9f9f9;
  max-width: 800px;
  margin: 0 auto;
  border-radius: 10px;
  border: 1px solid #ccc;
  padding: 20px;
  margin-top: 50px;
}

.quiz-question {
  padding-bottom: 10px;
  font-size: 18px;
  margin: 0;
}

.answer-label {
  display: block;
  font-size: 16px;
  margin-top: 15px;
}

.answer-input {
  width: calc(100% - 24px);
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  margin-top: 8px;
}

</style>