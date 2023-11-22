<template>
  <div>
    <h1>Community Page</h1>
    <RouterLink :to="{ name: 'CommunityCreateView' }">
      <button class="create">CREATE</button>
    </RouterLink>    
    <CommunityList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import CommunityList from '@/components/CommunityList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getCommunitys()
  // console.log(store.loginUser)
})

</script>

<style scoped>
  .create {
margin-left: 5px;
background-color: white;
box-shadow: gray 4px 4px 0px;
border-radius: 8px;
transition: transform 200ms, box-shadow 200ms;
margin-bottom: 30px;
color: black;
font-style: italic;
width: 6%;
  }

  
</style>
