<template>
  <div>
    <h3>Community List</h3>
    <CommunityListItem 
      v-for="community in store.communitys"
      :key="community.id"
      :community="community"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import CommunityListItem from '@/components/CommunityListItem.vue';

const store = useCounterStore()

// console.log(store.communitys)
</script>
