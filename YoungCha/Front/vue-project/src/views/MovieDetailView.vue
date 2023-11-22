<template>
  <div class="container" style="">
    <div class="row">
      <img  class="box col-4" v-if="movieDetails.poster_path" :src="`https://image.tmdb.org/t/p/w500/${movieDetails.poster_path}`" alt="포스터" >
      <div class="box position-relative col-8" style="font-size: 16px;">

        <div id="title"><h1>{{ movieDetails.title }}</h1></div>
        <div  id="overview">{{ movieDetails.overview }}</div>

        
        <div id="star" class="rating-box box w-100">
          <p id="point" style="margin-bottom: 0px;" class="">평점</p>
          <div class="star-container">
            <div v-for="star in 5" :key="star" class="star" @mouseover="hoverStar(star)" @mouseleave="resetStars" @click="setRating(star)">
              {{ star <= tempRating  ? '★' : '☆' }}
            </div>

          <!-- 코멘트 입력 -->
          </div>
          <p  id="onecomment" style="margin-bottom: 0px;   margin-bottom: 10px; ;" class="">한줄평</p>
          <div id="oneline">
            <input type="text" v-model.trim="Comment" style="width: 70%;"> 
            <input type="button" @click="saveRatingAndComment" value="작성">
          </div>


        </div>
      
      </div>  
    </div>
  </div>
  <br>
  <RouterLink 
    :to="{name: 'movies'}"
    :page="page"
    >

    <button class="btn-go-back" >돌아가기</button>
  </RouterLink>



  <RecommendedView/>

  <MovieComments/>
  

</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import axios from 'axios';
import {useRoute, useRouter } from 'vue-router';
import RecommendedView from '@/views/RecommendedView.vue';
import MovieComments from '@/views/MovieComments.vue';
import { useCounterStore } from '@/stores/counter';

const movieDetails = ref({});
const isSmallScreen = ref(false);
const route = useRoute();
const router = useRouter();
const userRating = ref(0);
const tempRating = ref(0);
const currentPage = ref(1);
const { movieId, page } = defineProps(['movieId', 'page'])
const store = useCounterStore()

const Comment = ref('');


const token = import.meta.env.VITE_TMDB_TOKEN
const trackPage = () => {
  const query = router.currentRoute.value;
}

  

  const goBack = () => {
    router.go(-1)
  }


const checkScreenSize = () => {
  isSmallScreen.value = window.innerWidth <= 768; // Adjust the breakpoint as needed
};

onMounted(() => {
  

checkScreenSize();
  window.addEventListener('resize', checkScreenSize);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', checkScreenSize);
});

onMounted(() => {
trackPage();
window.addEventListener('popstate', trackPage); // 뒤로 가기 버튼을 클릭할 때마다 페이지 추적
});

onBeforeUnmount(() => {
window.removeEventListener('popstate', trackPage); // 컴포넌트가 제거되기 전에 이벤트 리스너 제거
});

const setRating = (rating) => {
userRating.value = rating;
// 여기서 별점을 저장하거나 다른 동작을 수행할 수 있습니다.
};


const hoverStar = (star) => {
tempRating.value = star;
};

const resetStars = () => {
tempRating.value = userRating.value;
};

const saveRatingAndComment = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/movies/saveRatingAndComment/${route.params.movieId}/`,
    data: {
      rating: userRating.value,
     comment: Comment.value
    },
    headers: {
       Authorization: `Token ${store.token}`
     }
   })

.then(response => {
  console.log(response.data);
  router.push({ name: 'HomeView' }); // 변경: home 대신 실제 홈 화면의 이름을 사용

  // 성공적으로 저장한 후 추가 작업 수행

  // 예를 들어, 성공 메시지를 표시하거나 페이지를 새로고침하는 등의 작업 수행

})
.catch(error => {
  console.error('평점 및 코멘트 저장 중 에러 발생:', error);

  // 저장 실패 시 사용자에게 알림 또는 다른 작업 수행

});
};





(async () => {
  try {
    const response = await axios.get(`https://api.themoviedb.org/3/movie/${route.params.movieId}?language=ko-KR`, {
      headers: {
        Authorization: `Bearer ${import.meta.env.VITE_TMDB_TOKEN}`
      }
    });

    movieDetails.value = response.data;
  } 
    catch (error) {
    console.error('영화 정보를 가져오는 중 에러 발생:', error);
  }
})();



</script>

<style scoped>
/* 필요한 스타일링을 추가 */
.container {
  text-align: center; 
  background-color: black; 
  height:200%; 
  color: whitesmoke;
}
.box {
  border: 1px solid whitesmoke;
  padding: 20px;
  border-radius: 10px;
  background-color: black;
}

.rating-box {
  padding: 10px;
  border-radius: 5px;
  height: 30%;
  background-color: black;
}

#star{
  position: absolute;
  bottom: 0px;
  left:0;
}

#title {
  margin-top:20px;
  margin-bottom: 20px;
  background-color: black;
}
#overview {
  background-color: black;
  padding: 40px;

}
.star-container {
display: flex;
justify-content: center; /* 가로 가운데 정렬 */
align-items: center; /* 세로 가운데 정렬 */
background-color: black;
margin-bottom: 10px;
}

.star {
cursor: pointer;
font-size: 40px;
color: #eee;
margin-right: 5px;
background-color: black;
}

.star:hover {
color: #f82c60;
}
#oneline {
background-color: black;

}
#onecomment {
margin-bottom: 15px;  
}

.btn-go-back {
margin-top: 100px;
}


.back {
  scale: 130%;
  margin-top: 12%;
  margin-bottom: 5%;


}
</style>