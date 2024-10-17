<template>
  <section style="display:flex;">
    <div class="flex flex-col h-half">
      <div class="flex flex-row align-center mt-8 ml-3 text-2xl font-bold text-green-500 justify-between w-1/2 mx-auto">
        <p class="hover:opacity-70" @click="showAll()">
          Sport Articles 
        </p>
      </div>
      <div v-for="article in displayArticles.articles">
        <Article v-if="article.category.category=='Sports'" :article="article"/>
      </div>
    </div>
    <div class="flex flex-col h-half">
      <div class="flex flex-row align-center mt-8 ml-3 text-2xl font-bold text-green-500 justify-between w-1/2 mx-auto">
        <p class="hover:opacity-70" @click="showAll()">
          Politics Articles 
        </p>
      </div>
      <div v-for="article in displayArticles.articles">
        <Article v-if="article.category.category=='Politics'" :article="article"/>
      </div>
    </div>
    <div class="flex flex-col h-half">
      <div class="flex flex-row align-center mt-8 ml-3 text-2xl font-bold text-green-500 justify-between w-1/2 mx-auto">
        <p class="hover:opacity-70" @click="showAll()">
          Entertainment Articles 
        </p>
      </div>
      <div v-for="article in displayArticles.articles">
        <Article v-if="article.category.category=='Entertainment'" :article="article"/>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
    import { defineComponent } from "vue";
    import Article from "../components/Article.vue"
    import { ArticleType  } from '../interface.ts'
    import Cookies from 'js-cookie';
    import VueCookies from 'vue-cookies'
    import { useUserStore } from "../Stores/counter";
    import { User } from "../interface"


    export default defineComponent({
      components :{ Article },
        data(): {
          title: string,
          allArticles: ArticleType[]
          filteredArticles: ArticleType[]
          filtered: Boolean
          displayArticles: ArticleType[]
          displayFavorites: ArticleType[]
          showFavs: Boolean
          user: User
        }
        {
          return {
                title: "Main Page",
                allArticles: [],
                filteredArticles: [],
                filtered: false,
                displayArticles: [],
                displayFavorites: [],
                showFavs: false,
                user: {} as User

            }
        },
        methods:{
          showFav() :void {
            this.showFavs = true
          },
          showAll() :void {
            this.showFavs = false
          },
          filterArticles() :void {
            if(!this.filtered){
              this.displayArticles = this.filteredArticles 
            }
            else{
              this.displayArticles = this.allArticles
            }
          },
        },
        async mounted(): Promise<void>{
          const user  = Cookies.get('user');
            try {
            const response = await fetch(`http://localhost:8000/getFavouriteArticles/${user}`, {
                method: 'GET',
                credentials: "include",
                headers: {
                    "Content-Type": "application-json",
                    'X-CSRFToken': Cookies.get('csrftoken'), 
                },
                
            });
            if (response.ok) {
            this.displayArticles = await response.json();
            this.allArticles = this.displayArticles
            this.filteredArticles = this.displayArticles
        } 
        else {
          // Request failed, handle the error
          console.error('Request failed with status:', response.status);
        }
      } 
      catch (error) {
        console.error('An error occurred:', error);
      }
      try {
        const response = await fetch(`http://localhost:8000/users/${user}`, {
            method: 'GET',
            credentials: "include",
            headers: {
                "Content-Type": "application-json",
                'X-CSRFToken': Cookies.get('csrftoken'), 
            },
            
        });
        if (response.ok) {
          this.user = await response.json()
          const userStore = useUserStore()
          userStore.setUser(this.user.user[0])
          this.user = userStore.getUser
        } 
        else {
          // Request failed, handle the error
          console.error('Request failed with status:', response.status);
        }
      } 
      catch (error) {
        console.error('An error occurred:', error);
      }

          }
    })
</script>

<style scoped>
</style>
