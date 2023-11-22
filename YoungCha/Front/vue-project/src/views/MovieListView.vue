<template>
  <div>
    <h1 class="headtitle">Movie Pedia</h1>
    
    <br><hr>
    <div class="movies-container">
      <div class="movie" v-for="video in videos" :key="video.id" :video="video">
        <img :src="`https://image.tmdb.org/t/p/w500/${video.poster_path}`" alt="포스터" :page="page" :movieId="video.id" class="poster" @click="goToMovieDetail(video.id)"> <h2>{{ video.title }}</h2>
      </div>
    </div>
    <div class="page">
      <button @click="changePage(totalPages[0])">처음으로</button>
      <button v-for="page in displayedPages" :key="page" @click="changePage(page)" :disabled="currentPage === page">{{ page }}</button>
    </div>
    <button class="up" @click="scrollToTop">↑</button>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const page = ref(1);

const token = import.meta.env.VITE_TMDB_TOKEN


const videos = ref([])
const currentPage = ref(1)
const totalPages = ref(1)
const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}
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
      
      videos.value = res.data.results
      currentPage.value = res.data.page
      totalPages.value = res.data.total_pages
    })
    .catch(err => console.log(err))
}

const changePage = function(page) {
  currentPage.value = page
  searchVideo(page)

}

onMounted(() => {
  searchVideo()
})

const goToMovieDetail = function (movieId) {
  router.push(`/movie/${movieId}`)
}

const displayedPages = computed(() => {
  const pagesPerGroup = 10; // 한 그룹당 보여줄 페이지 수
  const groupNumber = Math.ceil(currentPage.value / pagesPerGroup);
  const startPage = (groupNumber - 1) * pagesPerGroup + 1;
  const endPage = Math.min(totalPages.value, startPage + pagesPerGroup - 1);

  return Array.from({ length: endPage - startPage + 2 }, (_, index) => index + startPage);
})
</script>

<style scoped>
.movies-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 3개의 열로 구성 */
  gap: 20px; /* 열 사이의 간격 */
  margin-left: 1%;
  row-gap: 30px;
  
  
}

.movie {
  text-align: center;
  max-width: 100%;
  
}

h1 {
  text-align: center;
  
  
}

.page {
  text-align: center;
  font-size: 100%;
  border: 3px black solid;
  background-color: black;
}

.page button {
  margin: 5px;
}

.up {
  position: fixed;
  bottom: 40px;
  right: 40px;
  font-size: 50px;
  background-color: black;
  color: white;
  border-radius: 50%;
  width: 80px;
  height: 80px;
  /* cursor: pointer; */
}

.headtitle {
  font-size: 50px;
  
}

.poster {
  width: 300px;
  height: 380px;
  
}

.poster h2{
  margin-top: -100px;
}
</style>
