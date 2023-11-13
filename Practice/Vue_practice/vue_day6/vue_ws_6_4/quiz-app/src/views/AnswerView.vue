<template>
  <div class="answer-page">
    <div class="title-section">
      <p>{{ pk }}번 문제</p>
      <h2>정답 확인</h2>
    </div>
    <div class="content-section">
      <!-- isCorrect 변수를 기반으로 정답 여부에 따라 클래스를 동적으로 설정 -->
      <h3 :class='{correct : isCorrect, incorrect : !isCorrect}'>{{ isCorrect ? '정답입니다!' : '오답입니다!' }}</h3>
      <p :class='{correct : isCorrect, incorrect : !isCorrect}'>나의 제출 답안 : {{ userAnswer }}</p>
      <p>정답 : {{ answer }}</p>
    </div>
  </div>
</template>

<script setup>
import {computed} from 'vue'
import {useRoute} from 'vue-router'



const route = useRoute()
const { pk, answer } = route.params         // 실제 문제 번호, 답안
const userAnswer = route.query.userAnswer   // 사용자가 작성한 답안

const isCorrect = computed(() => userAnswer === answer)

  
</script>

<style scoped>
.answer-page {
  background-color: #f9f9f9 ;
  max-width: 600px;
  margin: auto;
  margin-top: 50px ;
  padding: 20px;
  border: 1px solid #f5f5f5;
  border-radius: 10px;
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}


.title-section {
  text-align: center;
}


.content-section {
  background-color: white;
  padding: 20px;
  border: 1px solid;
  border-radius: 10px;
}

.correct {
  color: green;
}


.incorrect {
  color: red ;
}

</style>