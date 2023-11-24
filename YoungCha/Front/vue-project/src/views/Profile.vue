<template>
  <div style="margin-left: 30%; margin-top: 5%; margin-right: 25%; margin-bottom: 300px;" >
    <h1 style="color: rgb(50, 150, 80) ;">{{ route.params.nickname }}님의 프로필</h1>
    <br>
    <img src="@/assets/user.jpg" alt="usericon" class="usericon">
    <br>
    <button style="background-color: black; border: 1px solid black;" > 
      <RouterLink v-if="store.loginUser" style="font-size: 24px;" :to="{ name: 'account', params: {username: users.nickname}}" >개인정보수정</RouterLink>
    </button>
      <br>
      <button style="background-color: black; border: 1px solid black;">
      <RouterLink v-if="store.loginUser" style="font-size: 24px;" :to="{ name: 'PasswordChange'}">
        비밀번호 변경
      </RouterLink>
    </button>
    <br>
    <br>
    게시글 수 : {{ filterCommunityLength }}
    
    <hr>
    <form v-for="community in filterCommunity" :key="community.id">
      <div v-if="(route.params.nickname === community.user.nickname)">
        제목 : {{ community.title }}
        <br>
        내용 : {{ community.content }}
        <br>
        좋아요 : {{  community.like_community_users.length }}
        <hr>
      </div>
    </form>
    
    {{ route.params.nickname }}님의 선호 장르 목록 
    <div class="drop d-flex  " style="background-color: black; color: white;">
      <div class="btn-group">
        <button type="button" class="dropdown-toggle cta" data-bs-toggle="dropdown" aria-expanded="false">
          <p>
           선호장르 목록설정
          </p>
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
          <li><a class="dropdown-item" @click="sortBtn(10770, 'TV_영화')">TV 영화</a></li>
        </ul>
      </div>          
    </div>
    <div v-for="(state, genre) in Object.entries(toggleStates)" :key="genre" v-show="state[1].value">
      <div v-if="state[1].value">
        {{ state[0] }}
        <button @click="removeGenre(state)">삭제</button>
        
      </div>
    </div>
          
        
    
    <button style="background-color: black; border: 1px solid black;" > 
      <RouterLink v-if="store.loginUser" style="font-size: 34px;" :to="{ name:'movies'}" >>> [ 내 취향대로 추천받기 ] </RouterLink>
    </button>
    
    <hr>
  </div>
  <CommentListItem/>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
import {useCounterStore} from '@/stores/counter';
import {computed} from '@vue/reactivity'
import AccountView from '@/views/AccountView.vue';
import { RouterLink, RouterView } from 'vue-router'
import {ref} from 'vue';

const route = useRoute()
const store = useCounterStore()
const users = store.loginUser

const filterCommunity = computed(() => {
    return store.communitys.filter(community => route.params.nickname === community.user.nickname);
})

const filterCommunityLength = computed(() => {
    return filterCommunity.value.length;
});

const toggleStates = {
  모험: ref(false),
  판타지: ref(false),
  애니메이션: ref(false),
  드라마: ref(false),
  공포: ref(false),
  범죄: ref(false),
  액션: ref(false),
  코미디: ref(false),
  역사: ref(false),
  서부: ref(false),
  스릴러: ref(false),
  다큐멘터리: ref(false),
  SF: ref(false),
  미스터리: ref(false),
  음악: ref(false),
  로맨스: ref(false),
  가족: ref(false),
  전쟁: ref(false),
  TV_영화: ref(false),
};

const loadToggleStates = () => {
  // 로컬 스토리지에서 저장된 값 불러오기
  const savedStates = JSON.parse(localStorage.getItem('toggleStates'));
  if (savedStates) {
    Object.keys(toggleStates).forEach(genre => {
      if (savedStates[genre] !== undefined) {
        toggleStates[genre].value = savedStates[genre];
      }
    });
  }
};

const removeGenre = (genre) => {
  console.log('Removing genre:', genre);
  toggleStates[genre].value = false; 
  saveToggleStates();
  
};


const saveToggleStates = () => {
  // 로컬 스토리지에 현재 상태 저장
  const currentStates = {};
  Object.keys(toggleStates).forEach(genre => {
    currentStates[genre] = toggleStates[genre].value;
  });
  localStorage.setItem('toggleStates', JSON.stringify(currentStates));
};


const sortBtn = (genreId, genreName) => {
  toggleStates[genreName].value = true;
  saveToggleStates();
}



onMounted(loadToggleStates);

onMounted(() => {
   store.getMovieList()
   console.log(store.movieList)
})
</script>

<style scoped>
.usericon {
  width: 150px;
  border-radius: 30%;
  border: 5px solid rgb(50, 150, 80);
}

.drop {
  background-color: black;
  color: white;
}


</style>