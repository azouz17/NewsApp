<template>
    <div class=" flex flex-row align-baseline mt-12">
        <router-link class="" :to="{name: 'Main Page'}"><div class="">Back To Home</div></router-link>
    </div>
    <div class="rounded mt-8 p-4 flex flex-col">
        <div class="bg-[#FEF4EC]">
            <p class="text-2xl font-bold border-bottom border-black"> {{ article.title }}</p>
            <!-- <img src="../assets/vue.svg" width="100" height="100"> -->
             <img v-bind:src="article.articleImg" class="rounded border-grey border justify-center" width="300" height="200">

            <div class="mt-6">
                {{ article.text }}
            </div>
        </div>
        <div v-if="isAddCommentFormVisible" class="modal d-flex justify-content-center align-items-center" tabindex="-1" role="dialog">
        <div class="model-dialog" role="document" id="myModal">
            <div class="modal-content">
                <div class="modal-header text-center">
                    <h3 class="modal-title font-weight-bold">Add Comment</h3>
                    <button type="button" class="btn-close" @click="closeModal()"></button>
                </div> 
                <div class="modal-body">
                    <form @submit.prevent="addComment" class="p-3">
                        <label for="commentText" class="p-2">Comment</label>
                        <input type="text" v-model="newCommentText" required class="p-2 border border-dark"/>
                        <button type="submit" class="m-2 btn btn-dark">Add Comment</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
        <button class="btn btn-success col text-center" @click="showAddCommentForm">Add Comment</button>
        <p class=" text-2xl font-bold mt-4 "> Comments:</p>
        <div class="flex flex-col bg-[#FEF4EC] rounded">
            <div class="border-b border-black" v-for="comment in comments.articleComments">
                <div class="text-blue-500 ml-2 ">
                    {{ comment.user_fk.username }}:
                </div> 
                <div class="mt-1 font-bold ml-4">
                    {{ comment.comment }}
                </div> 
                <div  class="flex flex-col">
                    <CommentReplys :comment="comment"  />
                </div> 
                <div class="flex flex-row" v-if="comment.user_fk.id == user.id">
                    <p @click="enableEditCommentForm(comment.id)" class="text-blue-500 hover:text-blue-300 p-1 underline">Edit</p>
                    <p @click="removeComment(comment.id, comment.article_fk.id)" class="text-blue-500 hover:text-blue-300 p-1 ml-1 underline" >Delete</p>
                </div>           
            </div>
        </div>
        
        <div v-if="isEditComment" class="flex flex-col">
            <label>Edit:</label>
            <input class="border border-black rounded" v-model="editedComment">
            <div class="flex flex-row mt-3">
                <button class="border border-black rounded bg-grey w-14 p-1" @click="editComment()">Edit</button>
                <button class="border border-black rounded bg-grey w-14 ml-2 p-1" @click="isEditComment = false">Cancel</button>
            </div>
        </div>
    </div>
    
</template>

<script lang="ts">
    import { defineComponent } from "vue";
    import { RouterView } from "vue-router";
    import { useArticleStore } from "../Stores/counter";
    import { ArticleType, Comment, User } from "../interface"
    import { useUserStore } from "../Stores/counter";
    import Cookies from "js-cookie";
    import CommentReplys from '../Components/CommentReplys.vue'
    

    export default defineComponent({
        components: { RouterView, CommentReplys },
        data():  {
            article: ArticleType
            comments: Comment
            commentReplies: []
            isAddCommentFormVisible: boolean
            newCommentText: string
            user: User,
            isEditComment: Boolean,
            editedComment: String,
            comment_id: number,
        }{
            return{
                article: {} as ArticleType,
                comments: {} as Comment,
                commentReplies: [],
                isAddCommentFormVisible: false,
                newCommentText: '',
                user: {} as User,
                isEditComment: false,
                editedComment: "",
                comment_id: 0
            };
        },     
        methods: {
            closeModal() :void{
                this.isAddCommentFormVisible = false
            },
            enableEditCommentForm(id: number){
                this.isEditComment = true;
                this.comment_id = id
            },
            async getComments() {
                const temp: number= this.article.id
                try {
                    const response = await fetch(`http://localhost:8000/comments/${temp}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application-json',
                        'X-CSRFToken': Cookies.get('csrftoken'), 
                    },
                    credentials: 'include',
                    });
                    if (response.ok) {
                        const jsonResponse = await response.json();
                        this.comments = jsonResponse;
                        console.log(this.comments);
                    }
                    else{
                        console.error('Request failed!');
                    }
                }
                    catch(error) {
                        console.log(error);
                    }
            },
            async getCommentReplies(commentId: number) {
                try {
                    const response = await fetch(`http://localhost:8000/commentReplies/${commentId}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application-json',
                        'X-CSRFToken': Cookies.get('csrftoken'), 
                    },
                    credentials: 'include',
                    });
                    if (response.ok) {
                        const jsonResponse = await response.json();
                        this.commentReplies = jsonResponse;
                    }
                    else{
                        console.error('Request failed!');
                    }
                }
                    catch(error) {
                        console.log(error);
                    }
            },
             showAddCommentForm() {
                this.isAddCommentFormVisible = true;
            },
             hideAddCommentForm() {
                this.isAddCommentFormVisible = false;
            },
            async addComment() {
                try {
                    const response = await fetch(`http://localhost:8000/addArticleComment/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': Cookies.get('csrftoken'), 
                    },
                    body: JSON.stringify({
                        article_fk: this.article,
                        user_fk: this.user.id,
                        comment: this.newCommentText,
                        createdAt: new Date().toISOString(),
                    }),
                    credentials: 'include',
                    });
                    if (response.ok) {

                        this.isAddCommentFormVisible = false;
                    }
                    else{
                        console.error('Request failed!');
                    }
                }
                    catch(error) {
                        console.log(error);
                    }
                },
                async removeComment(commentId: number, article_id: number) {
                    try {
                        const response = await fetch(`http://localhost:8000/removeArticleComment/${commentId}/${article_id}`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application-json',
                            'X-CSRFToken': Cookies.get('csrftoken'), 
                        },
                        credentials: 'include',
                        });
                        if (response.ok) {
                            const jsonResponse = await response.json();
                            this.comments = jsonResponse;
                        }
                        else{
                            console.error('Request failed!');
                        }
                    }
                        catch(error) {
                            console.log(error);
                        }
                },
                async editComment() {
                    try {
                        const response = await fetch(`http://localhost:8000/editComment`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application-json',
                            'X-CSRFToken': Cookies.get('csrftoken'), 
                        },
                        credentials: 'include',
                        body: JSON.stringify({
                            comment: this.editedComment,
                            id:this.comment_id,
                            article_id: this.article.id
                        }),
                        });
                        if (response.ok) {

                            const jsonResponse = await response.json();
                            this.comments = jsonResponse;
                            this.isEditComment = false;
                            this.comment_id = 0
                            this.editedComment = ""
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
        mounted():void{
            const ArticleStore = useArticleStore()
            this.article = ArticleStore.getArticle
            const userStore = useUserStore()
            this.user = userStore.getUser
            this.getComments()
        }
    })
</script>