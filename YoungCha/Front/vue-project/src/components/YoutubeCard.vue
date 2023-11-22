<template>
  <!-- <div class="card-wrapper">
    <div class="card h-100">
      <img :src="thumbnailUrl" class="card-img-top" alt="..."
          @click="moveDetail"
        >
      <div class="card-body">
        <h6 class="card-title">{{ videoTitle }}</h6>        
      </div>
    </div>
  </div> -->

  <div class="card h-100">
  <div class="row g-0">
    <div class="col-md-4">
      <img :src="thumbnailUrl" class="img-fluid rounded-start" alt="..."
      data-bs-toggle="modal" :data-bs-target="`#${videoId}`"
    >
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{{ videoTitle }}</h5>        
      </div>
    </div>
  </div>
</div>
<div class="modal fade" :id="videoId" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">{{ videoTitle }}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <iframe id="ytplayer" type="text/html" width="640" height="360"
            :src="videoUrl"
            frameborder="0"></iframe>
      </div>
      
    </div>
  </div>
</div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router';

const router = useRouter()

const props = defineProps({
  video: Object,
})

const thumbnailUrl = computed(() => props.video.snippet.thumbnails.medium.url)
const videoTitle = computed(() => props.video.snippet.title)
const videoId = computed(() => props.video.id.videoId)
const videoUrl = computed(() => `https://www.youtube.com/embed/${videoId.value}`)
const moveDetail = function () {
  router.push({
    name: 'detail',
    params: { id: videoId.value }
  })
}
</script>

<style scoped>
/* .card-wrapper {
  width: 300px;
  height: 300px;
  margin: 1rem;
} */
.card {
  height: 200px;
  margin: 1rem;
}

</style>