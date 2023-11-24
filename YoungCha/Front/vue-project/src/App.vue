<template>
  <nav v-if="!store.isLogIn" style="border: 4px solid white;"  >
    <RouterLink :to="{ name: 'home' }">
      <img src="@/assets/logo.avif" alt="logo" style="position:absolute;" class="pic">
    </RouterLink> 
      <h2 class="logo-text">YOUNGcha</h2>
    <RouterLink style="font-size: 24px;" :to="{ name: 'movies' }">Movie List&nbsp;&nbsp;</RouterLink> 
    <RouterLink style="font-size: 24px;" :to="{ name: 'Search' }">Movie Serach&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'CommunityView' }">Community&nbsp;&nbsp;</RouterLink>
    
    <RouterLink style="font-size: 24px;" :to="{ name: 'SignUpView'}">SignUp&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'LogInView'}">LogIn&nbsp;&nbsp;</RouterLink>
  </nav>
  <nav v-if="store.isLogIn"  style="border: 4px solid white;"  >
    <RouterLink :to="{ name: 'home' }">
      <img src="@/assets/logo.avif" alt="logo" style="position:absolute;" class="pic">
    </RouterLink> 
      <h2 class="logo-text">YOUNGcha</h2>
    <RouterLink style="font-size: 24px;" :to="{ name: 'movies' }">Movie List&nbsp;&nbsp;</RouterLink> 
    <RouterLink style="font-size: 24px;" :to="{ name: 'Search' }">Movie Serach&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'CommunityView' }">Community&nbsp;&nbsp;</RouterLink>

    <RouterLink v-if="store.token !== null" style="font-size: 24px;" :to="{ name: 'profile', params: {nickname: users.nickname}}">Profile&nbsp;&nbsp;</RouterLink>
    
    <RouterLink style="font-size: 24px;" @click.prevent="logOut" :to="{ name: 'home'}">LogOut&nbsp;&nbsp;</RouterLink>
    <!-- <a @click="logOut" href="#" style="font-size: 24px;">
      LogOut
    </a> -->
  </nav>
  
  
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000" style=" width: 800px; height: 400px;" >
  <div class="carousel-inner">
    <div class="carousel-item active">
   
      <img class="d-block w-100" src="@/assets/polar.jpg" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="@/assets/aven.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="@/assets/dkn.jpg" alt="Third slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="@/assets/hobbit.jpg" alt="fourth slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="@/assets/incep.jpg" alt="fifth slide">
    </div>
  
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev" style="color: black;">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next" style="color: black;">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>


  <RouterView />
  <footer>
    <p>서비스 이용약관 | 커뮤니티 이용약관 | 개인정보 처리방침 | 법적고지 | 사이트 맵 | 고객센터 | 채용정보 </p>
    <p>주식회사 영차 | 서울특별시 서초구 강남대로 343 신덕빌딩 3층 |
사업자등록번호 211-88-66013 | 통신판매업 신고번호 제 2023-서울서초-0965호 |
호스팅 서비스 제공자 아마존웹서비시즈코리아 유한회사</p>
    
    <p>All Rights Reserved.</p>
    <br>
    <img src="@/assets/app2.PNG" alt="app"  >
    <img src="@/assets/apple2.PNG" alt="apple" >
    
    
    
    
  </footer>
</template>
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import axios from 'axios'


const store = useCounterStore()
const users = store.loginUser 
const TMDB_KEY = import.meta.env.VITE_TMDB_KEY 
var $ = jQuery.noConflict();

onMounted(() => {
  
  // store.isUser()
  if (store && store.loginUser) {
    console.log(store.loginUser);
  }
  
})

const logOut = () => {

  console.log('Headers:', {
    Authorization: `Token ${store.token}`
  });

    axios({
      method: 'post',
      url: `${store.API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then(res => {
      store.token = null
      store.loginUser = null
      console.log(res)
    })
    .catch(err => {
      console.log(err)
    })
  }
  
</script>
<style scoped>

#app {
font-family: 'Dancing Script';
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale;
text-align: center;
color: #2c3e50;
}

nav {
display: flex;
margin-top: 1px;
height: 80px;
background-color:black;
margin-bottom: 50px;
justify-content:end;
align-items: center;
}

nav a {
font-weight: bold;
color: white;
margin-right: 15px;
text-decoration: none;
}

nav a.router-link-exact-active {
color: rgb(100, 200, 150);
}
#nav_logo{
width: 55px;
height: 60px;
text-align: left;
margin-left: 25px;
margin-right: 150px;


}
.nav_box{
display: flex;
}
body{
background-color: #FFE4E1;
}
.pic {
width: 60px;
left: 13px;
top: 5.5px;


}

.logo-text {
color: white;
margin: 0;
font-size: 40px;
border: solid white 4px;
position: absolute;
left: 5%;

}
@media (max-width: 1255px) {
  .logo-text {
    opacity: 0; /* YOUNGcha 숨김 */
  }

nav {
flex-direction: column;
height: auto;
padding: 10px;
}

.nav-links {
margin-top: 10px;
}
}
</style>

<style>
div { 
  background-color:black;
  color: white;

}

hr {
 border: solid rgb(24, 253, 138) 4px ; 
}

footer {

  text-align: center;
  margin-top: 100px;

  
}

#carouselExampleControls {
  left: 30%;

}


 

</style>
