<template>
    <div>
      <button @click="openModal" class="btn border-white bg-black rounded text-white">Edit Profile</button>
      <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="absolute inset-0 bg-black opacity-50 z-40"></div>
  
        <div class="bg-white p-8 rounded shadow-md w-1/2 z-50 relative">
          <button @click="closeModal" class="absolute top-4 right-4 text-gray-700 hover:text-gray-900">
            ✕
          </button>
  
          <h2 class="text-2xl font-bold mb-4">Edit Profile</h2>
              <div class="flex flex-col items-start">
<!--                 <div class="flex flex-row mt-2">
                    <label class="font-bold">Username: </label>
                    <input type="text" class="ml-2 border border-black rounded p-0.5 flex" id="username" v-model="inputFields.name">
                </div> -->
                <div class="flex flex-row mt-2">
                    <label class="font-bold">Email: </label>
                    <input type="email" class="ml-2 border border-black rounded p-0.5 flex" id="Email" v-model="inputFields.email">
                </div>
                <div class="flex flex-row mt-2">
                    <label class="font-bold">Date of Birth: </label>
                    <input type="date" class="ml-2 border border-black rounded p-0.5 flex" id="username" v-model="inputFields.dob">
                </div>
                <div class="flex flex-row mt-2">
                    <label class="font-bold">Image: </label>
                    <input @change="onFileChange" type="file" class="ml-2" id="Image">
                </div>
                <!-- <div class="flex flex-row mt-2">
                  <span class="font-semibold">Favorite Category: </span>
                  <select class=" border rounded border-black w-24 ml-2" id="categories" name="categories" v-model="inputFields.category">
                      <option value="1" selected>temp</option>
                  </select>     
                </div> -->
              </div>
      
              <div class="mt-6 flex justify-end">
                <button @click="EditUser" class="rounded bg-green-500 text-white mr-2 p-2 font-bold">Edit</button>
                <button @click="closeModal" class=" border-white bg-gray-300 text-gray-700 rounded p-2 font-bold">Close</button>
              </div>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, PropType} from 'vue';
  import { useUserStore } from "../Stores/counter";
  import { User } from "../interface"
  import { Category } from "../interface";
  import Cookies from 'js-cookie';
 

  export default defineComponent({
    data(): { 
        user: User
        isModalOpen: boolean,
        inputFields: User
        categories: Category
    }{
      return{
        user: {} as User,
        isModalOpen: false,
        inputFields: {} as User,
        categories: {} as Category
      }
    },
    props:{
      userId: Number
    },
    methods: {
      openModal():void {
        this.isModalOpen = true;
      },
      closeModal():void {
        this.inputFields = {} as User
        this.isModalOpen = false;
      },
      async onFileChange(e) {
        const formData = new FormData();
        formData.append("profileImg", e.target.files[0]);
        const data = new URLSearchParams();
        data.append("profileImg", formData);

        console.log(formData);

        try{
            const response = await fetch(`http://localhost:8000/uploadProfileImg/${this.userId}`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': Cookies.get('csrftoken'), 
            },
            credentials: 'include',
            body: data,
          });
          if(response.ok) {
            const temp = await response.json()
            console.log(temp)
            // const userStore = useUserStore()
            // userStore.setUser(temp.user[0])
                                    
            // return this.closeModal()
          }
          else{
            console.log("Request Failed")
          }
        }
        catch(error){
            console.log(error)
        }
      },
      async EditUser() :Promise<void>{
      
          const data= {
            id: this.userId,
            name: this.inputFields.name,
            email: this.inputFields.email,
            dob: this.inputFields.dob,
          }
          try{

            const response = await fetch(`http://localhost:8000/editUser`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': Cookies.get('csrftoken'), 
            },
            credentials: 'include',
            body: JSON.stringify(data),
          });
          if(response.ok) {
            const temp = await response.json()
            console.log(temp)
            const userStore = useUserStore()
            userStore.setUser(temp.user[0])
                                    
            return this.closeModal()
          }
        else{
          console.log("Request Failed")
        }
      }
      catch(error){
          console.log(error)
      }
        }
      },
      validatefields():Boolean{
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const isValidEmail:Boolean = emailRegex.test(this.inputFields.email)
        const now = new Date("2023-12-12")
        const userDate = new Date(this.inputFields.dob)
       const isImage: Boolean = this.checkFile()
       if(isImage && this.inputFields.name && this.inputFields.email && userDate < now  && this.inputFields.dob){
        return true
       }
       else{
        return false
       }
      },
      checkFile() :Boolean{
        let result: boolean = false
        const fileInput = document.getElementById('Image');
        const file = fileInput.files[0];

      if (file) {
        const fileType = file.type;

        if (fileType.startsWith('image/')) {
          result = true
        } 
        else {
          
          }
        }
        return result
    }
  ,
  async mounted() :Promise<void>{
    const userStore = useUserStore()
    this.user = userStore.getUser
    console.log(this.user)
    this.inputFields.name = this.user.username;
    this.inputFields.email = this.user.email;
    this.inputFields.dob = this.user.dob;

  }

  });
  </script>
  
  