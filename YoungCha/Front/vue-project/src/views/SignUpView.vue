<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password1">password : </label>
      <input type="password" id="password1" v-model.trim="password1"><br>

      <label for="password2">password Confirm : </label>
      <input type="password" id="password2" v-model.trim="password2"><br>
      
      <label for="email">email : </label>
      <input type="email" id="email" placeholder="example@email.com" v-model.trim="email"><br>

      <label for="nickname">nickname : </label>
      <input type="text" id="nickname" v-model.trim="nickname"><br>


      <label for="age">age : </label>
      <input type="number" id="age" min="0" max="255" v-model.trim="age"><br>


      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const email = ref(null)
const age = ref(null)

const signUp = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    email: email.value,
    age: age.value
  }
  store.signUp(payload)
}
</script>

<style>

</style>
