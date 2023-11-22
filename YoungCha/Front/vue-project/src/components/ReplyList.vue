<template>
    <div>
        <ReplyListItem 
            v-for="reply in store.replies"
            :key="reply.id"
            :reply="reply"
            :commentId="commentId"
        />
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import ReplyListItem from '@/components/ReplyListItem.vue';

const { commentId } = defineProps(['commentId'])

const store = useCounterStore()
</script>

<style scoped>

</style>