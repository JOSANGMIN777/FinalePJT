<template>
    <div v-if="commentId === reply.comment.id">
      <p>{{ reply.user.nickname }} - {{ reply.content }}</p>
      <p>좋아요 - {{ reply.like_reply_users.length }}</p>
      <form @submit.prevent="deleteReply">
        <input type="submit" value="REPLY DELETE">
      </form>
      <form @submit.prevent="likeReply">
        <input type="submit" value="❤">
      </form>
    </div>
    

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

const deleteReply = () => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/reply/${reply.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
  .then((res) => {
    store.getComments()
    store.getReplies()
  })
  .catch((err) => {
    console.log(err)
  })
};


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