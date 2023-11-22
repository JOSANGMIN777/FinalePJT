<template>
  <div>
    <h1>홈 화면</h1>
    <div class="movies-container">
      <div class="movie" v-for="movie in randomMovies" :key="movie.id">
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="포스터" class="poster">
        <h2>{{ movie.title }}</h2>
      </div>
    </div>
  </div>
</template>
  
  <script setup>
  import { ref } from 'vue';

  const videos = ref([]);
  const props = defineProps(['movies']);

  const searchVideo = function(page = 1) {
  const url = `https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=${page}`
  const options = {
    url,
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: `Bearer ${token}`
    }
  };

  axios(options)
    .then(res => {
      const randomMovies = []
      for (let i = 0; i < 5; i++) {
        const randomIndex = Math.floor(Math.random() * res.data.results.length)
        const randomMovie = res.data.results[randomIndex]
        randomMovies.push({
          title: randomMovie.title,
          poster_path: randomMovie.poster_path
        })
      }

      videos.value = randomMovies
      currentPage.value = res.data.page
      totalPages.value = res.data.total_pages
    })
    .catch(err => console.log(err))
}
  </script>
  
  <style scoped>
  /* 필요한 스타일링을 추가 */
  </style>
  