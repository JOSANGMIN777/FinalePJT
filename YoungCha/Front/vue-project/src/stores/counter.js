import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const communitys = ref([])
  const comments = ref([])
  const replies = ref([])

  const movieList = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const loginUser = ref([])
  const movieList = ref([])

  // DRF에 Community 조회 요청을 보내는 action
  const getCommunitys = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/community/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        communitys.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const getComments = () => {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getReplies = () => {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/reply/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        replies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const signUp = (payload) => {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    const nickname = payload.nickname
    const email = payload.email
    const age = payload.age
    // const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, 
        password1, 
        password2,
        nickname,
        email,
        age,
      }
    })
      .then(res => {
        const password = password1
        logIn({ username, password })
      })
      .catch(err => console.log(err))
  }

  const logIn = (payload) => {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password,
      }
    })
      .then(res => {
        console.log(res)
        token.value = res.data.key
        router.push({ name: 'home' })
        isUser()
        // console.log
        // username.value = res.
      })
      .catch(err => console.log(err))
  }

  const logOut = () => {

  
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then(res => {
        token.value = null
        loginUser.value = null
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }

  const isLogIn = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const isUser = () => {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      loginUser.value = res.data
      // console.log(loginUser)
    })
    .catch(err => {
      console.log(err)
    })
  }


  const getMovieList = () => {
    axios({
      method: 'get',
      url: `${API_URL}/movies/movies/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) =>{
      // console.log(res)
      movieList.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const AccountUser = (payload) => {
    const nickname = payload.nickname
    const age = payload.age



    axios({
      method: 'put',
      url: `${API_URL}/accounts/user/`,
      data: {
        nickname,
        age
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      isUser()
      router.push({ name: 'profile', params:{nickname: payload.nickname}})
      
      
    })
    .catch(err => {
      console.log(err)
    })
  }


  const PasswordChange = (payload) => {
    const new_password1 = payload.new_password1
    const new_password2 = payload.new_password2

    axios({
      method: 'post',
      url: `${API_URL}/accounts/password/change/`,
      data: {
        new_password1,
        new_password2,
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      logOut()
      router.push({ name: 'home' })
    })
  }





  return { communitys, comments, replies, API_URL, getCommunitys, getComments, getReplies, signUp, logIn, logOut, token, isLogIn, loginUser, isUser, movieList, getMovieList, AccountUser, PasswordChange,}
}, { persist: true })
