<template>
  
     
  <div>
    <h1 class="headtitle"> Movie Pedia</h1>
    <div class="drop d-flex justify-content-center ">
            <div class="btn-group">
              <button type="button" class="dropdown-toggle cta" data-bs-toggle="dropdown" aria-expanded="false" >
                <h1 style="padding-left: 50px;">
                  장르별 카테고리
                </h1>
              </button>
              <ul style="border: 2px solid  rgb(62, 172, 62);" class="dropdown-menu">
                <li><a class="dropdown-item" @click="sortBtn(12, '모험')">모험</a></li>
                <li><a class="dropdown-item" @click="sortBtn(14, '판타지')">판타지</a></li>
                <li><a class="dropdown-item" @click="sortBtn(16, '애니메이션')">애니메이션</a></li>
                <li><a class="dropdown-item" @click="sortBtn(18, '드라마')">드라마</a></li>
                <li><a class="dropdown-item" @click="sortBtn(27, '공포')">공포</a></li>
                <li><a class="dropdown-item" @click="sortBtn(80, '범죄')">범죄</a></li>
                <li><a class="dropdown-item" @click="sortBtn(28, '액션')">액션</a></li>
                <li><a class="dropdown-item" @click="sortBtn(35, '코미디')">코미디</a></li>
                <li><a class="dropdown-item" @click="sortBtn(36, '역사')">역사</a></li>
                <li><a class="dropdown-item" @click="sortBtn(37, '서부')">서부</a></li>
                <li><a class="dropdown-item" @click="sortBtn(53, '스릴러')">스릴러</a></li>
                <li><a class="dropdown-item" @click="sortBtn(99, '다큐멘터리')">다큐멘터리</a></li>
                <li><a class="dropdown-item" @click="sortBtn(878, 'SF')">SF</a></li>
                <li><a class="dropdown-item" @click="sortBtn(9648, '미스터리')">미스터리</a></li>
                <li><a class="dropdown-item" @click="sortBtn(10402, '음악')">음악</a></li>
                <li><a class="dropdown-item" @click="sortBtn(10749, '로맨스')">로맨스</a></li>
                <li><a class="dropdown-item" @click="sortBtn(10751, '가족')">가족</a></li>
                <li><a class="dropdown-item" @click="sortBtn(10752, '전쟁')">전쟁</a></li>
                <li><a class="dropdown-item" @click="sortBtn(10770, 'TV 영화')">TV 영화</a></li>
              </ul>
            </div>          
          </div>
        </div>

      
      <br><hr>
      <div class="movies-container">
        <div class="movie" v-for="video in videos" :key="video.id" :video="video">
          <div v-if="video.genre_ids ">
            <img :src="`https://image.tmdb.org/t/p/w500/${video.poster_path}`" alt="포스터" :page="page" :movieId="video.id" class="poster" @click="goToMovieDetail(video.id)"> <h2>{{ video.title }}</h2>
          </div>
          
        </div>

    </div>

    <br>
    <div class="page">
      <button @click="changePage(totalPages[0])" style="width: 7%;">처음으로</button>
      <button v-for="page in displayedPages" :key="page" @click="changePage(page)" :disabled="currentPage === page">{{ page }}</button>
    </div>
    
    <div>

      
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
  const Buttons = ref(0)

  const sortBtn = (w, genre) => {
    Buttons.value= w
  searchVideo(w, 1)
  }
  
  
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    })
  }
  
  const searchVideo = (Btn, page) => {
    const genreIds = Btn !== 0 ? `&with_genres=${Btn}` : '';
    const url = `https://api.themoviedb.org/3/discover/movie?language=ko-KR&page=${page}${genreIds}`;

    
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
        
        videos.value = res.data.results;
        currentPage.value = res.data.page;
        totalPages.value = res.data.total_pages;
      })
      .catch(err => console.log(err))
  }
  
  const changePage = function(page) {
    currentPage.value = page
    searchVideo(Buttons.value, page)
  
  }
  
  onMounted(() => {
    searchVideo()
    console.log()
  
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
    cursor: pointer;
  
  }
  
  .movie :hover{
      color:  rgb(100, 200, 150);
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
    background-color: white;
  box-shadow: gray 4px 4px 0px;
  border-radius: 8px;
  transition: transform 200ms, box-shadow 200ms;
  margin-bottom: 30px;
  color: black;
  font-style: inherit;
  width: 4%;
  
  }
  
  .page button:active{
      transform: translateY(4px) translateX(4px);
      box-shadow: gray 0px 0px 0px;
    }
  
    .page button:hover{
      color:  rgb(100, 200, 150);
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
    cursor: pointer;
  }
  
  .up button:active{
      transform: translateY(4px) translateX(4px);
      box-shadow: gray 0px 0px 0px;
    }
  
  .movie button:active{
      transform: translateY(4px) translateX(4px);
      box-shadow: gray 0px 0px 0px;
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
  
  .headtitle{
    letter-spacing: 0px;
    background: linear-gradient(45deg, rgba(6, 63, 35), white, rgb(62, 172, 62), white);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    font-size: 70px;
  }
  
  .cta:hover::before{
      transform: scaleX(1.5) skewX(35deg);
  } 
  
  
  
  .cta:hover{
      color:  rgb(100, 200, 150);
  }
  
  .up:hover{
      color:  rgb(100, 200, 150);
  }
  
  .cta{
    
      font-size: 24px;
      display: inline-block;
      text-transform: uppercase;
      outline: 2px solid #FFF;
      padding: 1px 20px ;
      position: relative;
      overflow: hidden;
      transition: color 0.5s;
  }
  
  .drop {
    border: none;
    border-radius: 8px;
    background-color: white;
    font-weight:bold; 
  
  
    height: 100px;
    cursor: pointer;
    
    display: flex;
    justify-content: space-around;
    align-items: center;
  
    
    
    
  }
  
  .drop button {
    
    text-align: center;
    
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90%;
    border: none;
    background-color: white;
    
  }
  
  
  </style>
  