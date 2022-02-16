<template>
<div class="services">
   <div class="advert">
       <h2>Want funeral programmes printed?</h2>
       <p>Send us an email at beinafuservices@gmail.com. We will then send you a link of the various templates you can 
           choose from. We will themn print the programme according to your specifications. You can also choose from the ones below.
           We deliver what you ask for So please don't hesitate to reach out to us!
       </p>
       <hr>
       <p>For vendors, you can also consult with us. Some of our trusted vendors have been listed below.Contact them and all you needs will be met</p>
   </div>

    <h3 class="programmes-title">Printing funeral programmes and eulogies </h3>
    <div class="programmes">
         <img src="../assets/ff.webp" alt="">
         <img src="../assets/ff.webp" alt="">
         <img src="../assets/ff.webp" alt="">
         <img src="../assets/ff.webp" alt="">
    </div>

    <h3 class="vendors-title">We connect you to vendors who offer quality servie at affordble prices</h3>
    <div class="vendors">
        <div class="card">
             <img src="../assets/flower.jpg" alt="">
             <h4 class="title">Mave Sound Events</h4>
             <h4 class="contact"> tel +254 456 456</h4>
             <a href="">www.mavesound.com</a>
            
        </div>

         <div class="card">
             <img src="../assets/flower.jpg" alt="">
             <h4 class="title">Mave Sound Events</h4>
             <h4 class="contact">tel +254 456 456</h4>
             <a href="">www.mavesound.com</a>
            
        </div>

         <div class="card">
             <img src="../assets/flower.jpg" alt="">
             <h4 class="title">Mave Sound Events</h4>
             <h4 class="contact">tel +254 456 456</h4>
             <a href="">www.mavesound.com</a>
            
        </div>

         <div class="card">
             <img src="../assets/flower.jpg" alt="">
             <h4 class="title">Mave Sound Events</h4>
             <h4 class="contact">tel +254 456 456</h4>
             <a href="">www.mavesound.com</a>
            
        </div>
       
        
    </div>
    
   
    
    
    
</div>
    
</template>


<script>
export default {
    
}
</script>

<style scoped>

.services{
    width: 90%;
    margin: 0 auto;
    height: 100%;
    color: grey;
}

.advert h2{
  text-align: center;
  margin: 1em auto;
  color:#fbac0a;
  font-weight: 200;
}

.advert{
    width: 80vw;
    background-color: #ffff96;
    margin: 0 auto 2rem auto;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    color: grey;
    padding: 2em;
}

.advert hr{
  width: 90%;
  margin: 1em auto;
  border-bottom: 1px solid grey;
}


ul li{
    list-style-type: square;
    list-style-position: inside;
}

h3{
    color: #fbac0a;
}

h3.programmes-title{
    margin-bottom: 0.5rem;
    text-align: center;
}

.programmes,
.vendors{
   
    width: 90%;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin: 0 auto;
}

img{
    height: 20rem;
    
}

/* .vendors{
    background-color: red;
} */


.card{
    /* background-color: red; */
    width: 18rem;
    height: 24rem;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
   
    border-radius: 5px;
   
}



.card img{
    width: 100%;
    height: 50%;
    margin: 0 auto;
    
}
.card img:hover{
   opacity: 0.4;
    
}

h3.vendors-title{
    margin-top: 2rem;
    margin-bottom: -1rem;
    text-align: center;
   
    
}

.card a{
    color: grey;
    text-decoration: none;
}

.card a:hover{
    color: #fbac0a;

}
</style>