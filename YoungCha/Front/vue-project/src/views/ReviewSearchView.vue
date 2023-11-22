<template>
    <div>
      <SearchForm 
          @input-keyword="searchReview"
      />
      <div class="video-list">
        <YoutubeCard 
          v-for="video in reviewVideos" :key="video.etag"
          :video="video"
        />
      </div>    
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import SearchForm from '@/components/SearchForm.vue';
  import YoutubeCard from '@/components/YoutubeCard.vue';
  import axios from 'axios'
  const YOUTUBE_key = import.meta.env.VITE_YOUTUBE_API
  const reviewVideos = ref([])
  
  
  const saveData = function(data) {
    const jsonData = JSON.stringify(data)
    localStorage.setItem('review-videos', jsonData)
  }
  
  const loadData = function () {
    const jsonData = localStorage.getItem('review-videos')
    return JSON.parse(jsonData) || []
  }
  
  onMounted(() => {
    reviewVideos.value = loadData()
  })
  
  
  const searchReview = function (keyword) {
    const url = 'https://www.googleapis.com/youtube/v3/search'
    console.log(YOUTUBE_key)
    const params = {
      key: YOUTUBE_key,
      part: 'snippet',
      q: keyword,
      type: 'video',
    }
    axios({
      method: 'get',
      url,
      params,
    })
      .then(res => {
        console.log(res.data)
        reviewVideos.value = res.data.items
        saveData(reviewVideos.value)
      })
      .catch(err => console.log(err))
  }
  
  </script>
  
  <style scoped>
  
  </style>