<template>
    <div v-if="commentId === reply.comment.id">
        <p>{{ reply.user.nickname }} - {{ reply.content }}</p>
        <p>좋아요 - {{ reply.like_reply_users.length }}</p>
    </div>

    <form @click.prevent="likeReply">
        <input type="submit" value="❤">
    </form>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

// defineProps({
//     reply: Object,
//     commentId: Number,
// })

const store = useCounterStore()
const { reply, commentId } = defineProps(['reply', 'commentId'])


onMounted(
  console.log(reply)
)


const likeReply = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/reply/${reply.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    store.getCommunitys()
    store.getComments()
    store.getReplies()
    likeReplyCount()
  })
}

const likeReplyCount = () => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/reply/${reply.id}/like_count/`,
        headers: {
      Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
        console.log(reply)
    })
}
</script>

<style scoped>

</style>