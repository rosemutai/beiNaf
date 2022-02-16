<template>
  <div class="about">
    <div class="our-story">
      <h2>Why Bei Nafuu Events?</h2>
      <p>
        The society has always feared death since time memorial. Everyone is afraid to talk about it or to be
        associated with anything especially business related to the death. Hence the deceased are not accorded the 
        proper sendoff, moreso in not well to do families. Their legacies and life are forgotten as soon as they are buried.
      </p>
      <hr>
      <p>
        During funerals, what is talked about is more about their families and little about the individual, where they schooled, their hobies etc.
        Hence we decided as a company to come in, do research about the deceased and put in paper, so that it can be known. Their
        friends can come back later and see.
      </p>
    </div>
    <div class="mission">  

       <div class="mission-icon">
        <img src="../assets/mm.jpg" alt="">
      </div>

      <div class="title-description">
        <h4>Mission</h4>
        <p>We want every family to accord their lost one a good sendoff, regardless of their
          wealth status. This should be  affordable to every one. Lorem ipsum dolor sit amet 
          consectetur adipisicing elit. Provident dolore This should be  affordable to every one. 
          Lorem ipsum dolor sit amet This should be  affordable to every one. Lorem ipsum dolor sit amet 
          consectetur adipisicing elit. Provident dolore 
          consectetur adipisicing elit. Provident dolore alias sapiente quia esse nostrum
          at amet dicta error et!This should be consectetur adipisicing elit. Provi affordable to every one. Lorem ipsum
        </p>
      </div>

      
      
    </div>

    <div class="vision">
       <div class="vision-icon">
          <img src="../assets/vv.jpg" alt="">
      </div>
       <div class="title-description">
          <h4>Vision</h4>
          <p>To reach as many people as possible. Lorem ipsum
            dolor, sit amet consectetur adipisicing elit. This should be  affordable to every one. Lorem ipsum dolor sit amet 
          consectetur adipisicing elit. Provident dolore This should be  affordable to every one. Lorem ipsum dolor sit amet 
          consectetur adipisicing elit. Provident dolore 
            Voluptatem est corporis itaque, expedita, consectetur adipisicing elit. Provi
            consectetur adipisicing elit. Provi officiis illo ab laborum impedit quod
            sed cupiditate, accusamus labore nisi laudantium beatae soluta? Tempora, necessitatibus blanditiis?</p>
       </div>
     
    </div>
  </div>
</template>

<script>
export default {
  name: 'About'
}
</script>


<style scoped>


.our-story{
  width: 50vw;
  background-color: #ffff96;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  color: grey;
  padding: 2em;
}


.our-story hr{
  width: 90%;
  margin: 1em auto;
  border-bottom: 1px solid grey;
}


.our-story h2{
  text-align: center;
  margin: 1em auto;
  color:#fbac0a;
  font-weight: 200;
}

h4{
  color:#fbac0a;
  margin: 0.5em auto;

}

.mission,
.vision{
  display: flex;
  width: 70vw;
  color: grey;
  margin: 2rem 16%;
   /* background-color: red; */

}

.mission-icon,
.vision-icon{
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: auto 2rem;
}

.mission.title-description,
.vision.title-description{
  flex: 2;
  display: flex;
  flex-direction: column;
}

.title-description p{
  line-height: 2rem;
}

/* .mission.title-description p{
    order: 2;
  } */
 



@media screen and (max-width:768px) {
  .our-story{
    width: 90vw;
  }
  .mission,
  .vision{
    flex-direction: column;
  }

  h4{
    text-align: center;

  }

  

}




</style>
