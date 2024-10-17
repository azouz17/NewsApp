<template>
    <main class="container">
        <div class="border border-solid border-black h-20 mt-4 w-full rounded bg-[#86A0C1] text-white stroke-cyan-500 font-bold">
            <div class="text-2xl font-bold text-center align-baseline mt-2">Important News</div>
            <div class="flex flex-row justify-between px-2 mb-2">
                <button @click="logout">
                    <div class="text-left  px-2">Logout</div>
                </button>
                <router-link class="" :to="{name: 'Account Page'}"><div class="text-right text-white">Account</div></router-link>
            </div>   
       </div>
        <div>
            <router-link
                class=""
                :to="{name: 'Main Page'}"
            >
                
            </router-link>
        </div>
        <RouterView class="flex-shrink-0" />
    </main>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RouterView,  } from "vue-router";
import Cookies from 'js-cookie';
import { useUserStore } from "./Stores/counter";
export default defineComponent({
    components: { RouterView },
    methods:{
    async logout (){        
        try{
            const response = await fetch('http://localhost:8000/logout', {
                method:'POST',
                headers:{
                    'Content-Type': 'application-json',
                    'X-CSRFToken': Cookies.get('csrftoken'), 
                } ,
                credentials: 'include',
            })
            if(response.ok){
                console.log("blahh")
                const userStore = useUserStore()
                userStore.emptyUser()
                window.location.href = "http://localhost:8000";
                
            }
        }
        catch(error){
            console.log(error)
        }
    }
}
});



</script>

<style scoped>
</style>

