<template>
  <div class="quiz-item">
    <h4 class="quiz-question">{{ quiz.pk }}번 문제. {{ quiz.question }}</h4>
    <label :for="'answer' + quiz.pk" class="answer-label">정답 입력</label>
    <input 
      type="text" 
      :id="'answer' + quiz.pk" 
      class="answer-input"
      v-model="userAnswer"
      @keyup.enter="submitAnswer(quiz)"
    >
  </div>
</template>

<script setup>
import {ref} from 'vue'
import {useRouter} from 'vue-router'


// 부모 컴포넌트로부터 quiz 객체를 받아오는 props 선언
defineProps({
  quiz : Object
})

const router = useRouter()


// 사용자가 입력한 정답을 저장하는 변수
const userAnswer = ref('')


// 정답 제출 함수
const submitAnswer = (quiz) => {
  // console.log(quiz)

  // 라우터를 사용하여 정답 확인 화면으로 이동
  router.push(
    {
      // // 이동할 화면의 이름
      name : 'answer',

      // 라우트의 동적 매개변수(params) 설정
      params : {
        pk : quiz.pk,
        answer : quiz.answer
      },
    // 라우트의 쿼리 매개변수(query) 설정
      query : {
        userAnswer : userAnswer.value
      }
    }
  )
}


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