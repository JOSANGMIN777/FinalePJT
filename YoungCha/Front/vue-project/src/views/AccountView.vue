<template>
    <div>
        <h1>회원정보수정</h1>
        <form @submit.prevent="AccountUser">
            <p>현재 닉네임 - {{ route.params.username }}</p>
            <label for="nickname">변경할 닉네임 : </label>
            <input type="text" id="nickname" v-model.trim="nickname"><br>
            <br>
            <p>현재 나이 - {{ store.loginUser.age }}</p>
            <label for="age">변경할 나이 : </label>
            <input type="text" id="age" v-model.trim="age"><br>

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
const nickname = ref(null)
const age = ref(null)

const AccountUser = () => {
    const payload = {
        nickname: nickname.value,
        age: age.value,
    }
    store.AccountUser(payload)
}


</script>

<style scoped>

</style>