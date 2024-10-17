import { defineStore } from 'pinia';
import { ArticleType } from '../interface';
import { User } from '../interface';
import { useLocalStorage } from "@vueuse/core"

export const useArticleStore = defineStore('articles', {
  state: () => {
    return {
     article: useLocalStorage('articles', {} as ArticleType), //useLocalStorage takes in a key of 'count' and default value of 0
    };
  }, 
  getters: {
    getArticle: (state) => state.article,
  },
  actions: {
    setArticle(article: ArticleType): void {
      this.article = article; 
    },
  },
});

export const useUserStore = defineStore('user' , {
  state: () => {
    return {
     user: useLocalStorage('user', {} as User), //useLocalStorage takes in a key of 'count' and default value of 0
    };
  }, 
  getters:{
    getUser: (state) => state.user
  },
  actions:{
    setUser(user: User): void{
      this.user = user
    },
    emptyUser(user: User): void{
      console.log("blahh");
      this.user = {}
    }
  }
});