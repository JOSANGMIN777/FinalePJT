<template>
  <div>
    <h1 class="headtitle">Movie Pedia</h1>
    <br><hr>
    <div class="movies-container">
      <div class="movie" v-for="movie in randomMovies" :key="movie.id">
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="포스터" class="poster" @click="goToMovieDetail(movie.id)">
        <h2 id="title" @click="goToMovieDetail(movie.id)">{{ movie.title }}</h2>
        <h4>{{ movie.rating  }}</h4>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const token = import.meta.env.VITE_TMDB_TOKEN
const randomMovies = ref([])

const getRandomMovies = (movies, count) => {
  const uniqueMovies = new Set(); // 중복을 방지하기 위해 Set 사용
  while (uniqueMovies.size < count) {
    const randomIndex = Math.floor(Math.random() * movies.length);
    uniqueMovies.add(movies[randomIndex]);
  }
  return Array.from(uniqueMovies);
};

const goToMovieDetail = function (movieId) {
  router.push(`/movie/${movieId}`)
};

onMounted(async () => {
  const totalPages = 449; // 예시로 총 10페이지라고 가정
  const randomPage = Math.floor(Math.random() * totalPages) + 1; // 1부터 totalPages까지의 랜덤 페이지 번호 생성
  const url = `https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=${randomPage}`;

  try {
    const response = await axios.get(url, {
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${token}`,
      },
    });
    randomMovies.value = getRandomMovies(response.data.results, 5);
  } catch (error) {
    console.error(error);
  }
});
</script>

<style scoped>
img{
  height: 20%;
  width:20%;
}
#title{
  font-size: 30px;
}
</style>
