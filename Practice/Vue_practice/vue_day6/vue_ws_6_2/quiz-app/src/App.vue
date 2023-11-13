<template>
  <div class="quiz-app">
    <div class='app-header'>
      <h1>Quiz 퀴즈</h1>
    </div>
    <div class="app-subheader">
      <p>여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
    </div>
    <nav class="app-nav">
      <RouterLink to="/" class="nav-link">Home</RouterLink> |
      <RouterLink to="/quiz" class="nav-link">Quiz</RouterLink> |
    </nav>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

</script>

<style scoped>
.quiz-app {
  background-color: #f9f9f9;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  font-family: Arial, sans-serif;
}
.app-header {
  background-color: coral;
  color: white;
  padding: 15px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.app-subheader {
  background-color: white;
  padding: 45px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}

.app-nav {
  background-color: #333 ;
  color: white ;
  text-align: center;
  margin-top: 30px;
  padding: 10px 0;
  
}

.nav-link {
  color: white;
  padding: 10px 20px;
}

</style>