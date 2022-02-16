<template>
<div class="middle-banner">
    <div class="top">
        <div class="left-side">
            <h2>We are an events and Services providing Company in Kenya</h2>
            <p>Lorem ipsum dolor sit amet consectetur psum dolor sit amet consectetur
                psum dolor sit amet consectetur psum dolor sit amet consectetur adipisicing elit.
                laborum blanditiis vel quia est suscipit aliquam nesciunt nulla?</p>

            <button class="btn">More</button>
        </div>
        <div class="right-side">
            <img src="../assets/dove.png" alt="">
        </div>
    </div>
    <div class="bottom">
        <!-- <p>Lorem ipsum dolor sit amet consectetur
             adipisicing elit. Nobis accusantium adipisci
            omnis doloribus sit amet quisquam molestias, dolorum tempore officia!</p> -->
    </div>

    <div class="services">
        <div class="card">
            <div class="icon-title">
                <!-- <i class="fa fa-users fa-2x"></i> -->
                <img class="image-icon" src="../assets/people.png" alt="">
                <h4>Large Audience</h4>
            </div>
            
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing 
                dolor sit amet, consectetur adipisicing elit.
                Possimus eum qui dolorum fugit aspernatur.
                Cupiditate sit perspiciatis quia doloribus commodi?
            </p>
        </div>

         <div class="card">
             <div class="icon-title">
                 <!-- <i class="fa fa-check fa-2x"></i> -->
                  <img class="image-icon" src="../assets/services.png" alt="">
                 <h4>Quality Service</h4>
             </div>
              
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Possimus eum qui dolorum fugit aspernatur.
                Cupiditate sit perspiciatis quia doloribus commodi?
            </p>
        </div>

         <div class="card">
              <div class="icon-title">
                  <!-- <i class="fa fa-plug fa-2x"></i> -->
                   <img class="image-icon" src="../assets/ad.png" alt="">
                  <h4>Connect with Vendors</h4>
              </div>
             
             <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Possimus eum qui dolorum fugit aspernatur.
                Cupiditate sit perspiciatis quia doloribus commodi?
             </p>
        </div>

         <div class="card">
             <div class="icon-title">
                 <!-- <i class="fa fa-sticky-note fa-2x"></i> -->
                  <img class="image-icon" src="../assets/prog.png" alt="">
                 <h4>Event Programmes</h4>
             </div>
            
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Possimus eum qui dolorum fugit aspernatur.
                Cupiditate sit perspiciatis quia doloribus commodi?
            </p>
        </div>
    </div>

</div>
    
</template>

<script>
export default {
    
}
</script>


<style scoped>

.icon-title i{
    text-align: center;
    width: 100%;
    /* margin: 0.2em auto; */
}

.top{
    display: flex;
    width: 100%;
}

.image-icon{
    width: 10rem;
}

.left-side{
    /* background-color: blue; */
    flex: 2;
    display: flex;
    justify-content: center;
   
    flex-direction: column;
}



.left-side h2,
.left-side p{
    /* background-color: red; */
    color: grey;
    width: 60%;
    margin: 0 auto;
    padding: 1.2rem;
    line-height: 2em;
    
}

.left-side h2{
    color: #fbac0a;
}

.right-side{
    flex: 3;
    background-color: #ffff96;
    border-radius: 58% 62% 10% 50%;
   
}

img{
    width: 80%;
    margin-top: 1em;
    /* background-color: #ffff96; */
     /* border-radius: 58% 72% 10% 50%; */
   
   
}

.btn{
    /* background-color: #000; */
    color: #ffff96;
    width: 32%;
    margin: 0 0 0 24% ;
    padding: 1em 0;
    font-weight: 700;
    border-radius: 1.4rem;
    background-color: #fbac0a;
    color: #fff;
    /* margin-top: -4em; */
    border: transparent;
    text-transform: uppercase;
   

}


.services{
    width: 100%;
    /* background-color: red; */
    margin-top: 5rem;
    display: flex;
    justify-content: center;
}

.card{
    background-color: #fff;
    color: grey;
    margin: 1rem;
    width: 24rem;
    height: 28rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 13rem 5rem 20rem 11rem;
    border: 1px solid grey;
    

}

 .card:hover{
      border: 1px solid #fbac0a;
      transition: 1s 0.8s ease-in;
      /* box-shadow: 1px 1px 18px #fbac0a; */

    }
.card:hover img{
    transform: translateY(-20px);
    /* transform: rotate(-360deg); */
    transition:transform 1s 0.2s linear;
}

.card i{
    color: #fbac0a;
}

.card p{
    text-align: center;
    width: 70%;
    margin: 1em auto 0 auto;
}

@media screen and (max-width: 768px) {
    .top{
        display: flex;
        flex-direction: column;
    }

    .left-side{
        width: 90%;
        margin: 0 5%;
        /* background-color: red; */
    }

    .left-side p{
        /* background-color: red; */
        width: 95%;
    }

     .left-side h2{
         color: #fbac0a;
     }

    .right-side{
        width: 90%;
        margin: 2rem auto;
        background-color: #ffff96;
        border-radius: 58% 62% 10% 50%;
    }

    
    img{
        width: 100%;
        margin-top: 1em auto;
    }
    .services{
        
        flex-direction: column;
    }

    .card{
        /* background-color: red; */
        width: 80%;
        margin: 1rem auto;
        height: 28rem;
    }



    .left-side h2{
        font-size: 2rem;
        line-height: 3.4rem;
        
    }

    .left-side p{
        line-height: 1.6rem;
    }

    .card i{
       font-size: 2rem;
    }

    .btn{
        width: 50%;
    }

}

@media (min-width: 768px) and (max-width: 1024px) and (orientation: landscape) {
  
  .services{
      display: flex;
      /* background-color: red; */
      flex-wrap: wrap;
  }

  .btn{
      width: 50%;
  }

  .first-column{
      background-color: red;

  }
  
}

@media only screen and (min-device-width: 960px) {

    .services{
        flex-wrap: wrap;
    }

    .card{
        margin: 0.5rem;
        width: 22rem;
    }
  
 
  
}



</style>