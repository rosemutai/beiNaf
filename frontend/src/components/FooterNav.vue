<template>
<div class="footer">
   <div class="first-column">
       <div class="location">
           <i class="fa fa-map-marker"></i>
           <span>Tengecha Street, Kericho, Kenya</span>
       </div>

       <div class="phone">
           <i class="fa fa-phone"></i>
           <span>+254 565 766 567</span>
       </div>

       <div class="email">
           <i class="fa fa-envelope"></i>
           <span>beinafuuevents@gmail.com</span>
        
       </div>
   </div>
   <div class="second-column">
       <div class="about">
           <h5>About the Company</h5>
           <p>Lorem ipsum, dolor sit amet
                consectetur adipisicing elit. At aperiam explicabo maiores
                 accusantium ab earum?</p>
                
       </div>
       <div class="socials">
           <i class="fa fa-facebook "></i>
           <i class="fa fa-twitter"></i>
           <i class="fa fa-instagram"></i>
          
       </div>
   </div>

   <br>
   <br>
    
</div>
    
</template>

<script>
export default {
    name: 'Footer',
 
    
}
</script>


<style scoped>
.footer{
    width: 100vw;
    height: 40%;
    background-color: #fbac0a;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    color: #fff;
    margin-top: 1rem;

}

.first-column{ 
    display: flex;
    flex-direction: column;
    /* background-color: red; */
    justify-content: space-around;
    padding: 1em;
    

} 

.first-column div{
    margin: 1em;
}

.second-column{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
   
} 

.socials i{
    margin: 0.2em;
    text-align: center;
    font-size: 1.3rem;
}

.about p{
    width: 50%;
    padding: 1em 0;
  
}

span{
    margin-left: 0.5rem;
}



@media screen and (max-width: 768px) {
    .footer{
        flex-direction: column;
        align-items: center;
        justify-content: center;
        /* background-color: red; */
    }

    .first-column{
        margin-left: -12rem;

    }


    .about h5{
        width: 60%;
        margin: 1em auto;
    }


    .about p{
        padding-top: -1em;
        width: 60%;
        margin: -1em auto 0 auto;
        /* background-color: tomato; */
         /* background-color: red; */
    }

    .socials{
         /* background-color: blue; */
        margin-left: 9rem;
        /* background-color: red; */
    }
}

@media (min-width: 768px) and (max-width: 800px) and (orientation: landscape) {
  .footer{
       align-items: center;
       flex-direction: column;
       justify-content: flex-start;
  }

  .first-column{
      /* background-color: blue; */
      margin-left: -10rem;
      padding-left: -2rem;
      
  }
 
  .second-column{
      width: 70%;
      padding: 5em;
      margin: 0 auto;
  }

}

@media only screen and (min-device-width: 960px) {

    .footer{
       justify-content: space-between;
  }

  span{
    font-size: 1em;
}
  
  .first-column{
      /* background-color: red; */
      width: 100%;
      
  }
  
}

</style>