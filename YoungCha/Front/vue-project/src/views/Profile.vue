<template>
  <div style="margin-left: 30%; margin-top: 5%; margin-right: 25%; margin-bottom: 300px;" >
    <h1 style="color: rgb(50, 150, 80) ;">{{ route.params.nickname }}님의 프로필</h1>
    <br>
    <img src="@/assets/user.jpg" alt="usericon" class="usericon">
   
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
    </div>
<CommentListItem/>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
import {useCounterStore} from '@/stores/counter';
import {computed} from '@vue/reactivity'
const route = useRoute()
const store = useCounterStore()


const filterCommunity = computed(() => {
    return store.communitys.filter(community => route.params.nickname === community.user.nickname);
})

const filterCommunityLength = computed(() => {
    return filterCommunity.value.length;
});









onMounted(() => {
   
})
</script>

<style scoped>
.usericon {
  width: 150px;
  border-radius: 30%;
  border: 5px solid rgb(50, 150, 80);
}

</style>