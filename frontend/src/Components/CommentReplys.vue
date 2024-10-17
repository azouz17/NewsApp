<template>
    <div>
      <p @click="openModal" class="text-blue-500 hover:text-blue-300 p-1 underline">View Replys</p>
      <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="absolute inset-0 bg-black opacity-50 z-40"></div>
  
        <div class="bg-white p-8 rounded shadow-md w-1/2 z-50 relative">
          <button @click="closeModal" class="absolute top-4 right-4 text-gray-700 hover:text-gray-900">
            ✕
          </button>
  
          <h2 class="text-2xl font-bold mb-4">{{comment.comment}}</h2>
              <div class="flex flex-col items-start">
                <div class="border-b border-black" v-for="comment in commentReplies">
                    <div class="text-blue-500 ml-2 ">
                        {{ comment.user_fk.username }}:
                    </div> 
                    <div class="mt-1 font-bold ml-4">
                        {{ comment.comment }}
                    </div> 
                    
                    <!-- <div class="flex flex-row" v-if="comment.user_fk.id == user.id">
                        <p @click="enableEditCommentForm(comment.id)" class="text-blue-500 hover:text-blue-300 p-1 underline">Edit</p>
                        <p @click="removeComment(comment.id, comment.article_fk.id)" class="text-blue-500 hover:text-blue-300 p-1 ml-1 underline" >Delete</p>
                    </div>   -->         
                </div>

              </div>
      
              <div class="mt-6 flex justify-end">
                <div  class="flex flex-col">
                        <input class="border border-black rounded" v-model="commentReply">
                        <div class="flex flex-row mt-3">
                            <button class="border border-black rounded bg-grey w-14 p-1" @click="replyComment()">Send</button>
                        </div>
                    </div> 
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
        commentReplies: Category,
        commentReply: String
    }{
      return{
        user: {} as User,
        isModalOpen: false,
        commentReply: String,
        commentReplies: {} as Category
      }
    },
    props:{
      comment: Number
    },
    methods: {
      openModal():void {
        this.isModalOpen = true;
        this.getCommentReplies();
        this.commentReply = "";
      },
      closeModal():void {
        this.commentReply = {} as String
        this.isModalOpen = false;
      },
      async replyComment() :Promise<void>{
      
          const data= {
            comment_fk: this.comment,
            user_fk: this.user,
            comment: this.commentReply,
          }
          try{
            const response = await fetch(`http://localhost:8000/addCommentReply/`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': Cookies.get('csrftoken'), 
            },
            credentials: 'include',
            body: JSON.stringify(data),
          });
        if(response.ok) {
          const jsonResponse = await response.json();
          this.commentReplies = jsonResponse.commentReplys;
          this.commentReply = "";
          console.log(this.commentReplies)
                                  
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
      async getCommentReplies() {
        
              const temp = `http://localhost:8000/commentReplies/` + this.comment['id']
              try {
                  const response = await fetch(temp, {
                  method: 'GET',
                  headers: {
                      'Content-Type': 'application-json',
                      'X-CSRFToken': Cookies.get('csrftoken'), 
                  },
                  credentials: 'include',
                  });
                  if (response.ok) {
                      const jsonResponse = await response.json();
                      this.commentReplies = jsonResponse.commentReplys;
                      console.log(this.commentReplies)
                  }
                  else{
                      console.error('Request failed!');
                  }
              }
                  catch(error) {
                      console.log(error);
                  }
          },
      },
  async mounted() :Promise<void>{
    const userStore = useUserStore()
    this.user = userStore.getUser
    console.log(this.comment)
    // this.inputFields.name = this.user.username;
    // this.inputFields.email = this.user.email;
    // this.inputFields.dob = this.user.dob;
    


  }

  });
  </script>
  
  