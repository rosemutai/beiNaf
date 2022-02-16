<template>
<div class="navbar">
    <div class="logo">
        <h3>BeiNafuu Events</h3>
    </div>
    <div class="links">
        <router-link to="/">Home</router-link>
        <router-link  to="/about">About</router-link>
        <router-link to="/services">Services</router-link>
        <router-link to="/orbituaries">Orbituaries</router-link>
        <!-- <router-link  to="/anniversaries">Anniversaries</router-link> -->
        <router-link class="btn" to="/contact">Contact Us</router-link>
         
    </div>

    <div v-on:click="openMobileNav()" id="burger">
        <div class="line1"></div>
        <div class="line2"></div>
        <div class="line3"></div>
    </div>
    
</div>
    
</template>

<script>
export default {
    name: 'NavBar',
    props:
        ['links']
    ,
    methods:{
        openMobileNav(){
            const burger = document.getElementById('burger')
            const nav = document.querySelector('.links')
            // const navLinks = document.querySelectorAll('.links a')

            nav.classList.toggle('nav-active')
            burger.classList.toggle('toggle')
        }

    },
    mounted(){}

    
}
</script>


<style scoped>

.navbar{
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 5rem;
    /* background-color: red; */

}
    

.btn{
    color: #ffff96;
    padding: 0.6em;
    border-radius: 4px;
    background-color: #fbac0a;
    color: #fff;
    border: transparent;

}



.logo h3{
    color: grey;
}


.links a{
    color: grey;
    font-weight: 700;
    margin: 8px;
    text-decoration: none;
}

a.btn{
    color: #fff;
}

a:hover{
    background-color:  #fbac0a;
    /* #b6ccc4; */
    padding: 8px;
}

#burger div {
    width: 30px;
    height: 3px;
    margin: 8px;
    background-color: #fbac0a;
    transition: all 0.3s ease-in;
}

#burger {
    display: none;
    cursor: pointer;
}

@media screen and (max-width: 1024px) {
    .links{
        width: 50%
    }

}

@media screen and (max-width: 768px) {
    .links{
        position: absolute;
        height: 92vh;
        width: 100%;
        background-color: #ffff96;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;
        top: 8vh;
        right: 0;
        z-index: 3;
        padding: 100px;
        /* opacity: 0.8; */
        transform: translateX(100%);
        transition: transform 0.5s ease-out;
    }

    .nav-active{
        transform: translateX(0);
    }

    .toggle .line1 {
        transform: rotate(-45deg) translate(-9px, 10px);
    }
    
    .toggle .line2 {
        opacity: 0;
    }
    
    .toggle .line3 {
        transform: rotate(45deg) translate(-5px, -6px);
    }

    div#burger {
        display: block;
    }
}

@media (min-width: 768px) and (max-width: 800px) and (orientation: landscape) {
    .navbar{
        display: flex;
        justify-content: space-around;
        /* background-color: blue; */
    }
    .btn{
        /* background-color: red; */
       
        width: 100px;
    }

    .links{
        /* background-color: red; */
        margin-right: -2rem;
        width: 60%;
    }

}

/* @media only screen and (min-device-width: 960px) {
  
  .links{
      width: 60%;
      
  }
  
} */


</style>