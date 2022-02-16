<template>
<div class="orbituary-detail">
    <div class="person-descriptions">
        <img v-bind:src="person.photo" alt="">
       
         <!-- <img src="../assets/flower.jpg" alt=""> -->
        <div class="dates">
            <h2 >{{person.firstname}} {{person.lastname}}</h2>
            <h4>Sunrise: {{person['Date_of_Birth']}}</h4>
            <h4>Sunset:  {{person['Date_of_death']}}</h4>
            <!-- <h1>individual {{ $route.params.id }}</h1> -->
        </div>
         <h1 class="life-title">{{person.firstname}}'s Life History</h1>
        <div class="life-history">
            <p>{{person['Life_Description']}}</p>

        </div>
        
         <h1>Funeral Arrangements</h1>
        <div class="funeral-arrangements">
            <p>{{person['funeral_arrangements']}}</p>
        </div>
    </div> 
        <h1>Memories</h1>
    <div class="pictures">
        <div v-for="(image, index) in imageGallery" :key="index">
            <img :src="image.images">
        </div>
   
    </div>
   

    <div class="condolences-form">
        <h1>Leave a condolence note</h1>
        <CondolenceForm @send-condolence="writeCondolence"/>
        
    </div>
</div>
    
</template>

<script>
 import axios from 'axios'
import CondolenceForm from '@/components/CondolenceForm.vue'

export default {
    name: 'OrbituaryDetail',
    components:{
        CondolenceForm
    },
    props:['deceasedid'],

    data(){
        return{
            id: this.$route.params.id,
            person: {
                firstname: '',
                Middlename: '',
                lastname: '',
                Date_of_Birth: '',
                Date_of_death: '',
                Life_Description: '',
                photo: '',
            },
            imageGallery: [],

            condolenceNotes:[
                {
                    // deceasedid: '',
                    condoled_by: '',
                    message: ''
                }
            ],
        }
    },

    methods:{
        getDeceasedDetail(){
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/obituaries/${this.id}`
            })
            
            .then(response =>
               this.person = response.data
               
            )
            
        },

        // getDeceaseddetailInParent(){
        //     this.$emit('get-details', this.id)
        // },

        getDeceasedImages(){
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/obituaries/${this.id}/memories`
            }).then(response => {
                  let gallery = response.data //(this works well!!!!)
                  
                  this.imageGallery= gallery
                //   console.log(gallery)

            }
           
                
            )
        },


        writeCondolence(){
        if(this.condolenceNotes.condoled_by && this.condolenceNotes.message){
                axios({
                    method: 'post',
                    url: `http://127.0.0.1:8000/obituaries/${this.id}/condole`
                 
                   
                }).then(response =>{
                    console.log(response.data)
                    let deceasedcondolencenote = {
                        // 'deceasedid': this.id,
                        'condoled_by': this.condolenceNotes.condoled_by,
                        'message': this.condolenceNotes.message
                    }
                  

                    this.condolenceNotes.push(deceasedcondolencenote)
                    console.log(this.condolenceNotes)

                    this.condolenceNotes.condoled_by = '',
                    this.condolenceNotes.message = ''
                })
                .catch(error => {
                    console.log(error);
                })
                
            }
        }
    },

    mounted (){
        this.getDeceasedDetail()
    },

    created(){
        this.getDeceasedImages()
    }
}
   
</script>


<style scoped>
.person-descriptions img{
    width: 20rem;
    height: 20rem;
    border-radius: 50%;
    margin: 1rem 0;

}

h1{
    color: #fbac0a;
    text-align: center;
    font-weight: 200;
}

.life-title{
    margin-top: 1rem;
}

.person-descriptions{
    width: 80%;
    margin: 1rem auto;
    /* background-color: red; */
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    padding: 1rem;
    background-color: #ffff96;

}

.life-history p,
.funeral-arrangements p{
    margin: 1rem 2rem;
    /* background-color: red; */
}

hr{
    border: none;
    border-bottom: 1px solid grey;
    width: 80%;
    margin: 1rem auto;

}

.pictures{
    width: 80%;
    margin: 1rem auto;
    /* background-color: red; */
    padding: 0.5rem;
    display: flex;
    /* justify-content: center; */
    /* align-items: center; */
    flex-direction: row;
}

.pictures img{
    width: 15rem;
    margin: 0.5rem;
}



 

</style>