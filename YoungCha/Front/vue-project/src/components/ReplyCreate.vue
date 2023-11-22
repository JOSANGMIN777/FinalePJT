<template>
    <div>
      <form @submit.prevent="createReply">
        <label for="reply">대댓글 : </label>
        <input type="text" id="reply" v-model.trim="content">
        <input type="submit" >
      </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const content = ref(null)
const store = useCounterStore()

const { commentId } = defineProps(['commentId'])
// defineProps({
//     commentId: Number,
// })


const createReply = () => {
    axios({
        method: 'post',
        url: `${store.API_URL}/api/v1/comments/${commentId}/create/`,
        data: {
            content: content.value,
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
        store.getComments()
        store.getReplies()
        content.value = null
    })
    .catch((err) => {
        console.log(err.response.data)
    })
}

</script>

<style scoped>

</style>