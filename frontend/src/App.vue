<template>
  <div id="nav">
    <NavBar/>
     <!-- <hr> -->
   <router-view/>
   <br>
   <br>
   <br>
    <FooterNav/>
   
    
  </div>
  
</template>

<script>

import NavBar from './components/NavBar.vue'
import FooterNav from './components/FooterNav.vue'


export default {
  name: 'App',
  components: {
    NavBar,
    FooterNav
  }
}
</script>








<style>

#app {
  max-width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
 
  /* #D4A373; */
  font-family: 'Roboto', sans-serif;
  
}

hr{
  border: none;
  border-bottom: 1px solid #fbac0a;
  max-width: 90%;
  margin: 0 auto;
}


</style>
