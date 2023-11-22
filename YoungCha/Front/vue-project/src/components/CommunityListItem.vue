<template>
  <div>
    <RouterLink :to="{name: 'profile', params:{ nickname: community.user.nickname }}">
      <h4>{{ community.user.nickname }}</h4>
    </RouterLink>
    <h5>{{ community.id }}</h5>
    <p>{{ community.title }}</p>
    <p>{{ community.content }}</p>
    <p>{{ community }}</p>
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

const store = useCounterStore()

const { community } = defineProps(['community'])

const like_community = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/community/${community.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
}
</script>
