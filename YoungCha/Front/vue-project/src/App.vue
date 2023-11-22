<template>
  <nav v-if="!store.isLogIn">
    <RouterLink :to="{ name: 'home' }">
      <img src="@/assets/logo.avif" alt="logo" style="position:absolute;" class="pic">
    </RouterLink> 
      <h2 class="logo-text">YOUNGcha</h2>
    <RouterLink style="font-size: 24px;" :to="{ name: 'movies' }">Movie List&nbsp;&nbsp;</RouterLink> 
    <RouterLink style="font-size: 24px;" :to="{ name: 'Search' }">Movie Serach&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'CommunityView' }">Community&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'Recommend' }">Reviews&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'SignUpView'}">SignUp&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'LogInView'}">LogIn&nbsp;&nbsp;</RouterLink>
  </nav>
  <nav v-if="store.isLogIn">
    <RouterLink :to="{ name: 'home' }">
      <img src="@/assets/logo.avif" alt="logo" style="position:absolute;" class="pic">
    </RouterLink> 
      <h2 class="logo-text">YOUNGcha</h2>
    <RouterLink style="font-size: 24px;" :to="{ name: 'movies' }">Movie List&nbsp;&nbsp;</RouterLink> 
    <RouterLink style="font-size: 24px;" :to="{ name: 'Search' }">Movie Serach&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'CommunityView' }">Community&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'Recommend' }">Reviews&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'profile', params: {nickname: store.loginUser.nickname}}">Profile&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" :to="{ name: 'account', params: {username: store.loginUser.username}}">Account&nbsp;&nbsp;</RouterLink>
    <RouterLink style="font-size: 24px;" @click.prevent="logOut" :to="{ name: 'home'}">LogOut&nbsp;&nbsp;</RouterLink>
    <!-- <a @click="logOut" href="#" style="font-size: 24px;">
      LogOut
    </a> -->
    
    
  </nav>

<RouterView />
</template>
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import axios from 'axios'


const store = useCounterStore()
const TMDB_KEY = import.meta.env.VITE_TMDB_KEY 


onMounted(() => {
  
  // store.isUser()
  console.log(store.loginUser)
})

const logOut = () => {
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
width: 66px;
left: 10px;
top: 1px;

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

</style>
