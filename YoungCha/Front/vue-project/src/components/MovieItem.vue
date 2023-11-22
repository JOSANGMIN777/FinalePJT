<template>
    <div class="row">
      <div class="watch_list_box col mb-3" @click="completedMovie" :class="{'is-completed':movie.isCompleted}">
        <p class="mt-2 pt-2">{{movie.title}}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'WatchListItem',
    props:{
      movie: Object,
    },
    methods:{
      completedMovie() {
        this.$store.dispatch('completedMovie',this.movie)
      }
    }
  }
  </script>
  
  <style>
    .is-completed {
      text-decoration: line-through;
    }
    .watch_list_box{
      background-color: white;
      width: 100px;
      border-radius: 10px;
      text-align: center;
    }
  </style>