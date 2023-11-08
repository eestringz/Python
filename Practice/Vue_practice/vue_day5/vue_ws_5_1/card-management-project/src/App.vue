<template>
  <div class="app">
    <header>
      <h1>명함 관리 페이지</h1>
    </header>
    <main>
      <article>
        <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
      </article>
    </main>
    <footer>
      <p>&copy; 2023 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>

</script>

<style scoped>
.app {
  text-align: center;
  padding: 20px;
}

header {
  background-color: dodgerblue;
  color: #fff;
  padding: 20px;
  width: 100%;
  display: flex;
  justify-content: center;
  max-width: 300px;
  margin: 0 auto;
}

main {
  margin: 20px 0;
  padding: 10px;
  text-align: center;
}

article {
  padding: 20px;
  max-width: 100%;
  margin: 0 auto;
}

footer {
  background-color: ghostwhite;
  color: #000;
  width: 100%;
  position: absolute;
  bottom: 0;
  left: 0;
}
</style>