<template>
    <div class="condolence-form">
        <form v-on:submit.prevent="leaveCondolence" action="">
            <label for="firstname">Your Name</label>
            <input v-model="condolencenote.condoled_by" type="text" name="" id="firstame">

            <textarea  v-model="condolencenote.message" name="" id="" cols="30" rows="10" placeholder="leave a note"></textarea>

            <button type="submit" class="btn">Submit</button>
        </form>

    </div>
</template>

<script>

 
export default {
    name: 'CondolenceForm',
    props: ['data', 'index'],
    data(){
        return{
            condolencenote:{
                condoled_by: '',
                message: '',
            }
        }

    },

    methods:{
        leaveCondolence(){
            this.$emit("send-condolence", this.condolencenote.id)
        },

    }
    
}
</script>


<style scoped>

.condolence-form{
    width: 80%;
    margin: 1rem auto;
    /* background-color: red; */
}

form{
    display: flex;
    flex-direction: column;
    width: 80%;
    margin: 1rem auto;
    justify-content: space-between;
    /* background-color: #ffff96; */
}

label{
    margin: 0.5rem;
    color: grey;
}
input, textarea{
    width: 100%;
    margin: 0.5rem 0;
    border: none;
    outline: none;
    /* background-color: #ffff96; */
    border-bottom: 1px solid grey;
}


.btn{
    /* background-color: #000; */
    color: #ffff96;
    width: 16%;
    padding: 1em 0;
    font-weight: 700;
    border-radius: 4px;
    background-color: #fbac0a;
    color: #fff;
    margin: 0.5rem 0;
    border: transparent;
    text-transform: uppercase;

}

.btn:hover{
    opacity: 0.7;
}

</style>