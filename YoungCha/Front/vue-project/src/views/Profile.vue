<template>
    <div>
        <h1>{{ route.params.nickname }}의 Profile</h1>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()

onMounted(() => {

})
</script>

<style scoped>

</style>