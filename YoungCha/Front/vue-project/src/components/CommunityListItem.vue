<template>
  <div>
    <RouterLink :to="{name: 'profile', params:{ nickname: community.user.nickname }}">
      <h4>{{ community.user.nickname }}</h4>
    </RouterLink>
    <p>제목 - {{ community.title }}</p>
    <p>내용 - {{ community.content }}</p>
    <!-- <p>{{ store.comments }}</p> -->
    <p>좋아요 - {{ community.like_community_users.length }}</p>
    <form @submit.prevent="like_community">
      <input type="submit" value="❤">
    </form>
    <br>
    <form @submit.prevent="deleteCommunity">
      <input type="submit" value="DELETE">
    </form>
    <br>
    <RouterLink :to="{ name: 'CommunityDetailView', params: { id: community.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter';
import axios from 'axios'
import { onMounted } from 'vue';

const store = useCounterStore()

const { community } = defineProps(['community'])

const deleteCommunity = () => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/community/${community.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    store.getCommunitys()
  })
}

const like_community = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/community/${community.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    store.getCommunitys()
  })
}
</script>
