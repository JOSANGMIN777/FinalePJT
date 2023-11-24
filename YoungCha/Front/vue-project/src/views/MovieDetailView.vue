<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">

  <div class="container" style="">
    <div v-if="isBigScreen" class="row">
      <img  class="box col-4" v-if="movieDetails.poster_path" :src="`https://image.tmdb.org/t/p/w500/${movieDetails.poster_path}`" alt="포스터" >
      <div class="box position-relative col-8" style="font-size: 16px;">

        <div id="title"><h1>{{ movieDetails.title }}</h1></div>
        <div  id="overview">{{ movieDetails.overview }}</div>

        

        <div id="star" class="rating-box box w-100">
          <!-- <p id="point" style="margin-bottom: 0px;" class="">나의 평가</p> -->
          <div class="star-container">
            <div v-for="star in 5" :key="star" class="star" @mouseover="hoverStar(star)" @mouseleave="resetStars" @click="setRating(star)">
              {{ star <= tempRating  ? '★' : '☆' }}
            </div>

          </div>
          <div id="oneline">
            <input type="text" v-model.trim="Comment" style="width: 70%;"> 
            <input type="button" @click="saveRatingAndComment" value="작성" class="commit">
          </div>
        </div> 
      </div>  
    </div>  
    <div v-if="isSmallScreen" class="row">
      <img  class="box col-12" v-if="movieDetails.poster_path" :src="`https://image.tmdb.org/t/p/w500/${movieDetails.poster_path}`" alt="포스터" >
      <div id="underbox" class="box position-relative col-12" style="font-size: 16px;">

        <div id="title"><h1>{{ movieDetails.title }}</h1></div>
        <div  id="overview">{{ movieDetails.overview }}</div>
        
        <div id="star" class="rating-box box w-100">
          <p id="point" style="margin-bottom: 0px;" class="">나의 평가</p>
          <div class="star-container">
            <div v-for="star in 5" :key="star" class="star" @mouseover="hoverStar(star)" @mouseleave="resetStars" @click="setRating(star)">
              {{ star <= tempRating  ? '★' : '☆' }}
            </div>

          </div>
          <div id="oneline">
            <input type="text" v-model.trim="Comment" style="width: 70%;"> 
            <input type="button" @click="saveRatingAndComment" value="작성" class="commit">
          </div>
          

        </div>
        
      </div>   
    </div>
  </div>
  <br>
  <div id="commentbox" class="container">
    <div class="box row" v-for="(comment, index) in comments" :key="comment.id">
        <div class="col-md-3">
            <!-- Display stars based on rate_score -->
            <span v-for="i in ratings[index].rate_score" :key="i" class="fas fa-star text-warning"></span>
            <span v-for="i in 5 - ratings[index].rate_score" :key="i" class="far fa-star text-warning"></span>
        </div>
        <div class="col-md-3">
            {{ comment.user.nickname }}
        </div>
        <div class="col-md-6">
            {{ comment.content }}
        </div>
    </div>
</div>



  <RouterLink 
    :to="{name: 'movies'}"
    :page="page"
    >

    <button class="btn-go-back" >영화 둘러보기</button>
  </RouterLink>



  <!-- <RecommendedView/> -->

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
const route = useRoute();
const router = useRouter();
const userRating = ref(0);
const tempRating = ref(0);
const currentPage = ref(1);
const { movieId, page } = defineProps(['movieId', 'page'])
const store = useCounterStore()
const isBigScreen = ref(window.innerWidth >= 1000);
const isSmallScreen = ref(window.innerWidth < 1000);
const ratings = ref([]);
const comments = ref([]);
const Comment = ref('');

const token = import.meta.env.VITE_TMDB_TOKEN



onMounted(() => {
  getRatingsAndComments();
});


const trackPage = () => {
  const query = router.currentRoute.value;
}

  

  const goBack = () => {
    router.go(-1)
  }


const checkScreenSize = () => {
  isBigScreen.value = window.innerWidth >= 1000;
  isSmallScreen.value = window.innerWidth < 1000; 
};

onMounted(() => {


const isBigScreen = ref(window.innerWidth >= 1000);
const isSmallScreen = ref(window.innerWidth < 1000);

checkScreenSize();
  window.addEventListener('resize', checkScreenSize);
}); 

onBeforeUnmount(() => {
  window.removeEventListener('resize', checkScreenSize);
});

onMounted(() => {
trackPage();
window.addEventListener('popstate', trackPage); 
});

onBeforeUnmount(() => {
window.removeEventListener('popstate', trackPage); 
});

onMounted(() => {
  checkScreenSize();
  window.addEventListener('resize', checkScreenSize);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', checkScreenSize);
});

const setRating = (rating) => {
userRating.value = rating;
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
      comment: Comment.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(response => {
      console.log(response.data);
      // 코멘트를 제출하고 나면 페이지를 새로고침합니다.
      router.go(0);
    })
    .catch(error => {
      console.error('평점 및 코멘트 저장 중 에러 발생:', error);
    });
};

const getRatingsAndComments = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/movies/getRatingsAndComments/${route.params.movieId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
  .then(response => {
    console.log(response.data);
    // 서버에서 받은 데이터를 store에 저장할 수 있습니다.
    ratings.value = response.data.rates;
    comments.value = response.data.comments;
  })
  .catch(error => {
    console.error('평점 및 코멘트 조회 중 에러 발생:', error);
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
  font-size: 14px;

}
.star-container {
display: flex;
justify-content: center; 
align-items: center; 
background-color: black;
margin-bottom: 10px;
}

.star {
cursor: pointer;
font-size: 40px;
color:  rgb(100, 200, 150);
margin-right: 5px;
background-color: black;
}

.star:hover {
color:  rgb(100, 200, 150)
}
#oneline {
background-color: black;

}
#onecomment {
margin-bottom: 15px;  
}

.btn-go-back {
margin-top: 50px;
margin-left: 44%;
width : 200px;
height: 45px;
background-color: white;
box-shadow: gray 4px 4px 0px;
border-radius: 8px;
transition: transform 200ms, box-shadow 200ms;
margin-bottom: 30px;
color: black;
font-style: italic;
}

.btn-go-back:active{
    transform: translateY(4px) translateX(4px);
    box-shadow: gray 0px 0px 0px;
  }
.back {
  scale: 130%;
  margin-top: 12%;
  margin-bottom: 5%;


}

.commit {
background-color: white;
box-shadow: gray 4px 4px 0px;
border-radius: 8px;
transition: transform 200ms, box-shadow 200ms;
margin-bottom: 30px;
color: black;
font-style: italic;
margin-left: 2px;
width: 80px;
height: 40px;
}

.commit:active{
    transform: translateY(4px) translateX(4px);
    box-shadow: gray 0px 0px 0px;
  }

#underbox {
  height: 800px;
}

#commentbox {
  font-size: 20px;
  /* border: solid 1px white; */
  text-align: left;
}
</style>