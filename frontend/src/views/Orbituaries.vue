<template>
<div class="orbituary" v-if="deceased"> 
    <div class="person-card"  v-for="person in deceased" :key="person.id">
     
         <img v-bind:src="person.photo" alt="">
        <h3>{{person.firstname }} {{person.lastname }} {{person.deceasedid}}</h3>
        <h4>{{person['Date_of_Birth'] }} - {{person['Date_of_death'] }}</h4>
        <p> {{person['Life_Description'].slice(0, 100) + '...'}}</p>
       
        <router-link class="btn" :to="`/orbituaries/${person.deceasedid}`">More</router-link>
       
    </div> 
    
</div>
    
</template>

<script>

import axios from 'axios'

export default {
    name: 'Orbituaries',
    data(){
        return{
            deceased:{
                firstname: '',
                lastname: '',
                Date_of_Birth: null,
                Date_of_death: null,
                Life_Description: ''



            }
        }
    },
    methods:{
        getDeceasedPersons(){
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/obituaries'
            })
            .then(response => {
                this.deceased = response.data
            })

        }

        
    },

    created (){
        this.getDeceasedPersons()
    },

   
 
    
}
</script>


<style scoped>

.orbituary{
    width: 90%;
    margin: 0 auto;
    /* background-color: red; */
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.person-card{
    width: 20rem;
    height: 33rem;
    /* background-color: blue; */
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    margin: 2rem 1rem;
    border: 1px solid grey;
}

.person-card p{
        margin: 0.3em auto;
        width: 90%;
        
    }
    

.person-card img{
    width: 100%;
}

.btn:hover{
    opacity: 0.7;
}

.person-card h3,
.person-card h4{
    text-align: center;
}

a{
    text-decoration: none;
}


.btn{
    /* background-color: #000; */
    color: #ffff96;
    width: 32%;
    padding: 1em 0;
    font-weight: 700;
    border-radius: 4px;
    background-color: #fbac0a;
    color: #fff;
    margin: 0.8em auto;
    border: transparent;
    text-transform: uppercase;
    text-align: center;
   

}

@media screen and (max-width:768px){
    .person-card{
        width: 80%;
        margin: 1rem 5%;
        height: 38rem;
    }

    .person-card p{
        margin: 0.3em auto;
        width: 90%;
        /* background-color: red; */
    }
    
}


</style>