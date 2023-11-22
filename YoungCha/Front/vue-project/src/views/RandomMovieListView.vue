<template>
    <div>
      <h2>랜덤 5개의 영화</h2>
      <ul>
        <li v-for="video in videos" :key="video.id">
          {{ video.title }}
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';

  const videos = ref([]);
  const props = defineProps(['movies']);
  
  </script>
  
  <style scoped>
  /* 필요한 스타일링을 추가 */
  </style>
  