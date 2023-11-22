<template>
  <div class="search-form">
  <form @submit.prevent="inputKeyword">
      <div class="input-group mb-3">
          <input type="text" class="form-control" placeholder="검색어를 입력해 주세요."
          v-model="keyword"
          >
          <button class="btn btn-outline-" >검색</button>
      </div>
  </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const keyword = ref('')

const emit = defineEmits()

const inputKeyword = function () {
  console.log(keyword.value)
  emit('inputKeyword', keyword.value)
}
</script>

<style scoped>

.search-form {
  margin:1rem;
}
.btn-outline- {
  
  background-color: black;
  color: white;
}

</style>