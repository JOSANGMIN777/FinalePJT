<template>
  <div>
    
    <CommentListItem 
      v-for="comment in store.comments"
      :key="comment.id"
      :comment="comment"
      :communityId="communityId"
      :community="community"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import CommentListItem from '@/components/CommentListItem.vue';
const { communityId, community } = defineProps(['communityId', 'community'])

const store = useCounterStore()

</script>

<style scoped>

</style>