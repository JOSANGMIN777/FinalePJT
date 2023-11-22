<template>
  <div>
    작성자 :
    <RouterLink :to="{name: 'profile', params:{ nickname: community.user.nickname }}">
    
      <button class="username">
        {{ community.user.nickname }}

      </button>
    </RouterLink>
    <h5>{{ community.id }}</h5>
    <p>{{ community.title }}</p>
    <p>{{ community.content }}</p>
    
    <RouterLink :to="{ name: 'CommunityDetailView', params: { id: community.id }}">
      <button class="detail">DETAIL</button>
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
<style scoped>
.detail {
margin: 5px;
background-color: white;
box-shadow: gray 4px 4px 0px;
border-radius: 8px;
transition: transform 200ms, box-shadow 200ms;
margin-bottom: 30px;
color: black;
font-style: italic;
}

.username {
  margin: 5px;
  background-color: white;
box-shadow: gray 4px 4px 0px;
border-radius: 8px;
transition: transform 200ms, box-shadow 200ms;
margin-bottom: 30px;
color: black;
font-style: italic;
}
</style>
