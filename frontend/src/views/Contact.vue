<template>
    <div class="contact">
        <form v-on:submit.prevent="contactUs" >
            <label for="firstname">First Name</label>
            <input v-model="firstname" type="text" name="" id="firstame">

            <label for="lastname">Last Name</label>
            <input v-model="lastname" type="text" name="" id="lastame">

            <label for="email">Email</label>
            <input v-model="email" type="email" name="" id="email">

            <label for="phone">Phone</label>
            <input v-model="phone" type="text" name="" id="phone">

            <label for="subject">Subject</label>
            <input v-model="subject" type="text" name="" id="subject">

            <label for="message">Message</label>
            <input v-model="message" type="text" name="" id="message">

            <button type="submit" class="btn">Submit</button>
        </form>

        <!-- <div class="alert-message" v-if="submitted">
            alert("hey")
        </div> -->
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Contact',
    data(){
        return{
            contacts: [],
            firstname: '',
            lastname: '',
            email: '',
            phone: '',
            subject: '',
            message: '',
            submitted: false,
            success_msg: "Thank you for contacting us, we will get to you as soon as possible"

        }
    },
    methods:{
        contactUs(){
            if(this.firstname && this.lastname && this.email && this.phone && this.subject && this.message){
                axios({
                    method: 'post',
                    url: 'http://127.0.0.1:8000/contact',
                    data:{
                        firstname: this.firstname,
                        lastname: this.lastname,
                        email: this.email,
                        phone: this.phone,
                        subject: this.subject,
                        message: this.message

                    }
                }).then((response) =>{
                    let newContact = {
                        'id': response.data.id,
                        'firstname': this.firstname,
                        'lastname': this.lastname,
                        'email': this.email,
                        'phone': this.phone,
                        'subject': this.subject,
                        'message': this.message

                    }

                    this.contacts.push(newContact)
                    this.firstname = ''
                    this.lastname = ''
                    this.email = ''
                    this.phone = ''
                    this.subject = ''
                    this.message = ''


                })
                .catch((error) =>{
                    console.log(error)
                })
            }
        }
    }
    
}
</script>


<style scoped>
.contact{
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
input{
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
    margin: 0.8rem auto;
    border: transparent;
    text-transform: uppercase;
}

.btn:hover{
    opacity: 0.7;
}

@media screen and (max-width: 768px){

    form{
        width: 100%;
    }

}


</style>