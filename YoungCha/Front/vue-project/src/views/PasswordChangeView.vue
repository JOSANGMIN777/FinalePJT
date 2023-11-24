<template>
    <div>
        <h1>비밀번호 변경</h1>
        <form @submit.prevent="PasswordChange">
            <label for="new_password1">비밀 번호 : </label>
            <input type="password" id="new_password1" v-model.trim="new_password1"><br>
            <br>

            <label for="new_password2">비밀 번호 확인 : </label>
            <input type="password" id="new_password2" v-model.trim="new_password2"><br>

            <input type="submit">
        </form>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import { useRoute } from 'vue-router';
import { ref } from 'vue';

const route = useRoute()
const store = useCounterStore()
const new_password1 = ref(null)
const new_password2 = ref(null)


const PasswordChange = () => {
    const payload = {
        new_password1: new_password1.value,
        new_password2: new_password2.value,
    }
    store.PasswordChange(payload)
}

</script>

<style scoped>

</style>