<template>
    <div>
        <h1>회원정보수정</h1>
        <form v-for="movie in store.movieList" :key="movie.id">
            <p v-if="movie.genre_check.includes(12)">
                {{ movie.genre_check }}
            </p>

        </form>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

const store = useCounterStore()

// onMounted(() => {
//     store.getMovieList()
// })

// const filterMovieList = computed(() => {
//     return store.movieList.filter(movie => movie.)
// })
</script>

<style scoped>

</style>