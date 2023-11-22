<template>
    <div v-if="commentId === reply.comment.id">
        <p>{{ reply.user.nickname }} - {{ reply.content }}</p>
    </div>
</template>

<script setup>
defineProps({
    reply: Object,
    commentId: Number,
})
</script>

<style scoped>

</style>