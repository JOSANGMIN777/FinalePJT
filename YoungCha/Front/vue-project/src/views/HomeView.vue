<template >
  <div>
    <h1 class="headtitle" style="text-align: center;">Welcome to Youngcha</h1>
    <br><hr>
    <LoginMain/>
    <!-- <button @click="Reroll">새 목록 가져오기</button> -->
    <div style="text-align: center;">
      <img src="@/assets/start.png" alt="" @click="Reroll" style="width: 20%;">
    </div>
    <br>
    <br><br>
    <br>
    <br>


    <div class="movies-container" style="margin-bottom: 500px;">
      <div class="arrow left" @click="rotateMovies(-1)">&#9665;</div>
      <div class="movie" v-for="(movie, index) in randomMovies" :key="movie.id" :style="getMovieStyle(index)">
        <div class="movie-content">
          <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="포스터" class="poster" @click="goToMovieDetail(movie.id)">
          <h2 id="title" @click="goToMovieDetail(movie.id)">{{ movie.title }}</h2>
          <h4> ★ : {{ movie.vote_average }}</h4>
           
          <!-- <h4>{{ movie.rating }}</h4> -->
        </div>
      </div>
      <div class="arrow right" @click="rotateMovies(1)">&#9655;</div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import LoginMain from '@/views/LoginMain.vue';


const router = useRouter();
const token = import.meta.env.VITE_TMDB_TOKEN;
const randomMovies = ref([]);
const currentIndex = ref(2); // 현재 중앙에 위치한 포스터의 인덱스

const getRandomMovies = (movies, count) => {
  const uniqueMovies = new Set();
  while (uniqueMovies.size < count) {
    const randomIndex = Math.floor(Math.random() * movies.length);
    uniqueMovies.add(movies[randomIndex]);
  }
  return Array.from(uniqueMovies);
};

const getMovieStyle = (index) => {
  const baseSize = [330, 330, 330, 330, 330];
  const baseFontSize = [30, 30, 30, 30, 30]; // 추가: 각 포스터에 대한 기본 글씨 크기
  const scaleFactor = 1 / 1.4;
  const distance = index - currentIndex.value;

  const size = baseSize[index] * Math.pow(scaleFactor, Math.abs(distance) * 1.1);
  const fontSize = baseFontSize[index] * Math.pow(scaleFactor, Math.abs(distance) * 1.1); // 추가: 글씨 크기 계산
  const position = distance * 140;

  return {
    zIndex: randomMovies.value.length - Math.abs(distance),
    transform: `translateX(${position}px) scale(${1 - Math.abs(distance) * 0.15})`,
    width: `${size}px`,
    fontSize: `${fontSize}px`, // 추가: 글씨 크기 적용
  };
};

const goToMovieDetail = function (movieId) {
  router.push(`/movie/${movieId}`);
};

const rotateMovies = (direction) => {
  currentIndex.value = (currentIndex.value + direction + randomMovies.value.length) % randomMovies.value.length;
};

onMounted(async () => {
  const totalPages = 449;
  const randomPage = Math.floor(Math.random() * totalPages) + 1;
  const url = `https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=${randomPage}`;

  try {
    const response = await axios.get(url, {
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${token}`,
      },
    });
    randomMovies.value = getRandomMovies(response.data.results, 5);
  } catch (error) {
    console.error(error);
  }
});

const Reroll = async () => {
  const totalPages = 449;
  const randomPage = Math.floor(Math.random() * totalPages) + 1;
  const url = `https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=${randomPage}`;

  try {
    const response = await axios.get(url, {
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${token}`,
      },
    });
    randomMovies.value = getRandomMovies(response.data.results, 5);
  } catch (error) {
    console.error(error);
  }
};
</script>

<style scoped>
.movies-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 40px; 
  position: relative;
  transition: none; /* 애니메이션 비활성화 */
}

.arrow {
  position: absolute;
  top: 50%;
  font-size: 30px;
  cursor: pointer;
}

.left {
  left: 0;
}

.right {
  right: 0;
}

.movie {
  text-align: center;
  position: relative;
  transition: transform 0.3s ease-in-out, width 0.3s ease-in-out;
}

.poster {
  width: 100%;
  height: auto;
}

#title {
  font-size: 30px;
  margin-bottom: 20px;
}
img {
  margin-top: 20px;
  margin-bottom: 20px;
}
h4 {
  color: yellow;
}

</style>
