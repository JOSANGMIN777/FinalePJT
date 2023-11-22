<template>
    <div>
      <h1>홈 화면</h1>
      <!-- <MovieListView :movies="allMovies"/> -->
      <RandomMovieListView :movies="randomMovies"/>
    </div>
  </template>
  
  <script setup>
  import MovieListView from '@/views/MovieListView.vue';
  import RandomMovieListView from '@/views/RandomMovieListView.vue';
  import axios from 'axios';
  import { ref } from 'vue';

  const allMovies = ref([]);
  const randomMovies = ref([]);
  
  // // 모든 영화 목록 가져오기
  // axios.get('/api/v1/movies/')
  //   .then(response => {
  //     allMovies.value = response.data;
  //   })
  //   .catch(error => {
  //     console.error('영화 목록을 가져오는 중 에러 발생:', error);
  //   });
  
  // // 랜덤으로 5개의 영화 목록 가져오기
  axios.get('/api/v1/movies/random/')
    .then(response => {
      randomMovies.value = response.data;
    })
    .catch(error => {
      console.error('랜덤 영화 목록을 가져오는 중 에러 발생:', error);
    });
  </script>
  
  <style scoped>
  </style>