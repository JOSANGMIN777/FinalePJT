<template>
  <div>
    <form @submit.prevent="createComment">
      <label for="comment">댓글 : </label>
      <input type="text" id="comment" v-model.trim="content">
      <input type="submit" >
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';

const content = ref(null)
const store = useCounterStore()

const { communityId } = defineProps(['communityId'])
// defineProps({
//   communityId: Number,
// })


const createComment = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/community/${communityId}/create/`,
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
  console.log(err.response.data);
  // console.log(err.response.status);
  // console.log(err.response.headers);
})
}

</script>

<style scoped>

</style>