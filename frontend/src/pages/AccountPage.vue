<template>
    <div class=" flex flex-row align-baseline mt-12">
        <router-link class="" :to="{name: 'Main Page'}"><div class="">Back To Home</div></router-link>
    </div>
    <div class="flex flex-col h-64 items-center">
        <div class="w-2/3 text-center">
            <p class="text-4xl font-bold">Account</p>
            <div>
                <img :src="user.profileImg" class="" width="200" height="100" alt="No Profile image"> 
            </div>
            <div class="text-left mt-8 w-full">
                <div class="flex flex-row">
                    <p class="font-semibold">Username :</p>
                    <span class="ml-2"> {{ user.username }}</span>
                </div>
                <div class="flex flex-row">
                    <p class="font-semibold">Email :</p>
                    <span class="ml-2">{{ user.email }}</span>
                </div>
                <div class="flex flex-row">
                    <p class="font-semibold">Date Of Birth :</p>
                    <span class="ml-2"> {{ user.dob }}</span>
                </div>
                <div class="flex flex-row">
                    <span class="font-semibold">Favorite Category: </span>
                    <div v-for="favcat in favCategories">
                        <p class="ml-2 border-right" @click="removeFavouriteCategory(favcat.id)">{{ favcat.category }} [-]</p>
                    </div>
                </div>
                <div class="flex flex-row">
                    <span class="font-semibold">Add Other Categories To You Favourites: </span>
                    <div v-for="cat in nonFavcategories">
                        <p class="ml-2 border-right" @click="addFavouriteCategory(cat)">{{ cat.category }} [+]</p>
                    </div>
                </div>
            </div>
            <Modal :userId="user.id"  />
        </div>
    </div>
 <!--    <div class="flex flex-col h-64 items-center">
    </div> -->
</template>

<script lang="ts">
import { defineComponent} from 'vue';
import { storeToRefs } from 'pinia'
import {RouterView} from 'vue-router'
import Modal from '../Components/Modal.vue'
import { useUserStore } from "../Stores/counter";
import { User } from "../interface"
import Cookies from 'js-cookie';


export default defineComponent({
    components: { RouterView, Modal},
    data(): {
        user: User
        favCategories: [],
        nonFavcategories: [],
    }{
        return{
            user: {} as User,
            favCategories: [],
            nonFavcategories: [],
        }
    },
    methods:{
        removeCommonElements(array1: any[], array2: any[]): any[] {
          const result: any[] = [];

          for (const element1 of array1) {

            let found = false;

            // Check if the current element in array1 is present in array2
            for (const element2 of array2) {
                if (element1.id == element2.category_fk) {
                    found = true;
                    break;
                }
            }

            // If the element is not found in array2, add it to the result
            if (!found) {
              result.push(element1);
            }
          }

          return result;
        },
        async addFavouriteCategory(category_fk:any) {
            try {
                const response = await fetch(`http://localhost:8000/addFavouriteCategory`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application-json',
                    'X-CSRFToken': Cookies.get('csrftoken'), 
                },
                credentials: 'include',
                body: JSON.stringify({
                    category_fk: category_fk,
                    user_fk: this.user.id,
                    createdAt: new Date().toISOString(),
                }),
                });
                if (response.ok) {
                    const jsonResponse = await response.json();
                    this.favCategories = jsonResponse.favouriteCategories
                    this.nonFavcategories = this.removeCommonElements(this.nonFavcategories, this.favCategories)
    
                }
                else{
                    console.error('Request failed!');
                }
            }
                catch(error) {
                    console.log(error);
                }
            },
        async removeFavouriteCategory(id) {
            const data = {
                id: id,
                user_fk: this.user.id,
            }
            try {
                const response = await fetch('http://localhost:8000/removeFavouriteCategory', {
                    method: 'DELETE',
                    headers: {
                    'Content-Type': 'application-json',
                    'X-CSRFToken': Cookies.get('csrftoken'), 
                },
                    credentials: 'include',
                    body: JSON.stringify(data)
                });
                if (response.ok) {
                    const jsonResponse = await response.json();
                    this.favCategories = jsonResponse.favouriteCategories
                    this.getCategories()
                    this.nonFavcategories = this.removeCommonElements(this.nonFavcategories, this.favCategories)
                } 
                else {
                  // Request failed, handle the error
                  console.error('Request failed with status:', response.status);
                }
            } 
                catch (error) {
                console.error('An error occurred:', error);
            }
        },
        async getCategories(){
            try{
                const response  = await fetch(`http://localhost:8000/categories` ,{
                  method: 'GET',
                  headers: {
                    'Content-Type': 'application-json',
                    'X-CSRFToken': Cookies.get('csrftoken'), 
                },
                credentials: 'include',
                })
                if(response.ok) {
                  const jsonResponse = await response.json()
                   this.nonFavcategories = jsonResponse.categories
                   this.nonFavcategories = this.removeCommonElements(this.nonFavcategories, this.favCategories)
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
    
    async mounted():Promise<void>{
        const userStore = useUserStore()
        this.user = userStore.getUser
        try {
            const response = await fetch(`http://localhost:8000/favoriteCategory/${this.user.id}` , {
                method: 'GET',
                headers: {
                    'Content-Type': 'application-json',
                    'X-CSRFToken': Cookies.get('csrftoken'), 
                },
                credentials: 'include',
            });
            if (response.ok) {
                const jsonResponse = await response.json();
                this.favCategories = jsonResponse.favouriteCategories
            }else{
                console.error('Request failed!');
            }
        }catch(error) {
            console.log(error);
        }

        this.getCategories()
    
    }

})
</script>