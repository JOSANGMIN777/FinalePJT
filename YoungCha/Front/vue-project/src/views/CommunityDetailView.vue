<template>
  <div>
    <h1>Detail</h1>
    <div v-if="community">
      <p>제목 : {{ community.title }}</p>
      <p>내용 : {{ community.content }}</p>
      <p>작성일 : {{ community.created_at }}</p>
      <p>수정일 : {{ community.updated_at }}</p>
      <p>댓글 수 : {{ community.comments.length }}</p>
      <hr>
      <div>
        <CommentCreate 
          :communityId="community.id"
        />
        <hr>
        <CommentList 
          :communityId="community.id"
          :community="community"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
import CommentCreate from '@/components/CommentCreate.vue'
import CommentList from '@/components/CommentList.vue'


const store = useCounterStore()
const route = useRoute()
const community = ref(null)

onMounted(() => {
  store.getCommunitys()
  store.getComments()
  store.getReplies()

  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/community/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      community.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<style>

</style>
