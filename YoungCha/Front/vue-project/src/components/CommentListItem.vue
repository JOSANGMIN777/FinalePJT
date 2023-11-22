<template>
  <div v-if="communityId === comment.community.id">
    {{ comment.user.nickname }} - {{ comment.content }}
    <p>
      좋아요 - {{ comment.like_comment_users.length }}
    </p>
      
    <form @submit.prevent="deleteComment">
      <input type="submit" value="DELETE">
    </form>
    <form @click="likeComment">
      <input type="submit" value="❤">
    </form>
    <div>
      <ReplyCreate 
        :commentId="comment.id"
      />
      <ReplyList 
        :commentId="comment.id"
      />
    </div>
    <hr>
  </div>
</template>

<script setup>
import ReplyCreate from '@/components/ReplyCreate.vue';
import ReplyList from '@/components/ReplyList.vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted } from 'vue';

// defineProps({
//   comment: Object,
//   communityId: Number,
//   // commentId: Number,
// })
const { communityId, comment } = defineProps(['communityId', 'comment'])
const store = useCounterStore()


onMounted(
  console.log(comment)
)

const deleteComment = () => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/comments/${comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    store.getCommunitys()
    store.getComments()
    store.getReplies()
  })
}

const likeComment = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/comments/${comment.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    store.getCommunitys()
    store.getComments()
    store.getReplies()
  })
}

</script>

<style scoped>

</style>