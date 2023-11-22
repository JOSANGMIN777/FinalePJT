<template>
    <div id="Main">
        
        <p> 당신을 위한 무작위 영화 5선</p> 
               <!-- <img src="@/assets/start.png" alt="" id="reroll" @click=""> -->
        CLICK TO REROLL
        <br>
        <p style="font-weight: 500;">↓↓</p>
    </div>


</template>

<script setup>

import { onMounted, ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const gotologin = function () {
  router.push(`/login`)
}
</script>

<style  scoped>
#Main {
    text-align: center;
    font-size: 50px;
}
img {
    width:150px;
}
p {
        font-weight: 600;
}

</style>