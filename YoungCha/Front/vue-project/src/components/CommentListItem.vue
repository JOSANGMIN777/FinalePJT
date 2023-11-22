<template>
  <div v-if="communityId === comment.community.id">

    {{ comment.user.nickname }} - {{ comment.content }} - {{ comment.id }}



    <form @submit.prevent="deleteComment">
      <input type="submit" value="DELETE">
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

// defineProps({
//   comment: Object,
//   communityId: Number,
//   // commentId: Number,
// })
const { communityId, comment } = defineProps(['communityId', 'comment'])
const store = useCounterStore()

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

</script>

<style scoped>

</style>