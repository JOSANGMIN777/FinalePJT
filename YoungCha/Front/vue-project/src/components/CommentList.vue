<template>
  <div>
    
    <CommentListItem 
      v-for="comment in store.comments"
      :key="comment.id"
      :comment="comment"
      :communityId="communityId"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import CommentListItem from '@/components/CommentListItem.vue';
const { communityId } = defineProps(['communityId'])

const store = useCounterStore()

</script>

<style scoped>

</style>