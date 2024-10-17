<template>
        <div class="flex flex-col border border-black rounded w-3/4 mx-auto mt-8 p-3 hover:opacity-70 bg-[#F5F4F6]" @click="navigateToArticle()">
            <p class="text-2xl font-bold border-bottom border-[#e3e3e3] border-solid p-1 ">{{ article.title }}</p>
            <p class="italic ">{{ article.text }}</p>
            <!-- {{ path }} -->
            <img v-bind:src="article.articleImg" class="rounded border-grey border justify-center" width="300" height="200">
            <p class="italic">Posted on: {{ article.createdAt }}</p>
        </div>
</template>

<script lang="ts">
    import { defineComponent, PropType } from "vue";
    import { RouterView } from "vue-router";
    import { useArticleStore } from '../Stores/counter.js';
    import { ArticleType  } from '../interface.ts'

    export default defineComponent({
        components: { RouterView },
        data(): {
            path:string

        }{
            return{ 
            }
        },
        props: {
            article: {
            type: Object as PropType<ArticleType>,
            required: true,
    },

        },
        methods:{
            navigateToArticle() {
    
                const ArticleStore = useArticleStore();
                // Set the selected article in the store
                ArticleStore.setArticle( this.article);
                const temp: ArticleType =  ArticleStore.getArticle
                this.$router.push('/Article');
            },
            getImgUrl(file) {
                var images = require.context('../assets/categoryImgs/', false, /\.jpg$/)
                console.log(images);
                return images('./' + file + ".jpg")
            }
        },
        mounted(){
            // this.path = "../assets/articleImgs/PSG.jpg"
            this.path = "PSG"
            console.log(this.article);
        },
        computed: {
          imagePath(image) {
            if (image !== '') {
              return require(`@/assets/categoryImgs/${image}`);
            }
          }
        }

    })

</script>