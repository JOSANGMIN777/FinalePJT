<template>
    <div>
      <ul class="nav navbar-dark bg-dark">
        <li class="nav-item">
          <RouterLink :to="{ name: 'home'}" class="nav-link ">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'movies'}" class="nav-link text-white">영화조회</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'reviewSearch'}" class="nav-link text-white">Review</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'recommended'}" class="nav-link text-white">Recommended</RouterLink>
        </li>
  </ul>
    </div>
  </template>
  
  
  <script setup>
    import { RouterLink, RouterView } from 'vue-router'
  </script>
  
  
  <style scoped>
  
  </style>