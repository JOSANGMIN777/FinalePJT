<template>
  <div>
    <h1>Community Page</h1>
    <RouterLink :to="{ name: 'CommunityCreateView' }">
      [CREATE]
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

<style>

</style>
