from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import json
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login 
from django.contrib.auth.decorators import login_required



from django.contrib.auth.hashers import make_password, check_password

def main_spa(request: HttpRequest) -> HttpResponse:
    print(request)
    form = LogInForm()
    return render(request, 'api/spa/login.html', {'form': form})

# @api_view(['GET'])

# @csrf_exempt
# View to get user by user id
def getUsers(request,user_id):
    print(user_id)
    user = User.objects.filter(id = user_id)
    return_list = []
    for item in user:
        return_list.append(item.to_dict())
    return JsonResponse({
        'user': return_list
    })


# @csrf_exempt
# view used to authenticate user and log them in
def logIn(request):
    print('inside method')
    form = LogInForm()
    if request.method == 'POST':
        print('inside if')
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if(user is not None):
            print('foud user')
            auth.login(request, user)
            response = HttpResponseRedirect('http://localhost:5173/')
            response.set_cookie('user', str(user.id), max_age=3600, secure=True)
            return response
        print(' didnt foud user')
        
    return render(request, 'api/spa/login.html', {'form': form})


    
# @csrf_exempt
# view to log user out
def logout(request):
    print('logged ot user')
    form = LogInForm()
    auth.logout(request)
    return HttpResponseRedirect('http://localhost:8000/')


# @csrf_exempt
# view to add user to database (sign up)
def addUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("thanks!", form)
        if form.is_valid():
            print("thanks!!!!", form.cleaned_data)
            new_user = User.objects.create(
                username = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                password = make_password(form.cleaned_data['password']),
                # profileImg = form.cleaned_data['profileImg'],
            )

            user = authenticate(username=request.POST['name'], password=request.POST['password'])
            auth.login(request, user)
            response = HttpResponseRedirect('http://localhost:5173/')
            response.set_cookie('user', str(user.id), max_age=3600, secure=True)
            return response
    else:
        form = SignUpForm()

    return render(request, 'api/spa/signup.html', {'form': form})

@csrf_exempt
#view that enables users to edit their profile
def editUser(request):
   EDIT = json.loads(request.body)
   User.objects.filter(id= EDIT['id'] ).update(name = EDIT['name'], email = EDIT['email'], dob = EDIT['dob'])
   return getUsers(request, EDIT['id'])


#view to upload profile pic
def uploadProfileImg(request, id):
    print("in up method")
    print(request.POST.get('profileImg'))
    print(request.FILES.getlist('profileImg'))
    # EDIT = json.loads(request.body)
    # User.objects.filter(id= EDIT['id'] ).update(name = EDIT['name'], email = EDIT['email'], dob = EDIT['dob'])
    try:
        file = request.data['profileImg']
    except KeyError:
        raise ParseError('Request has no resource file attached')
    new_profile = User.objects.filter(id=id).update(profileImg=file)

    return getUsers(request, EDIT['id'])

# @csrf_exempt
# view to delete user
def deleteUser(request):
     DELETE = json.loads(request.body)
     user = User.objects.get(id=DELETE['id'])
     user.delete()
     return getUsers(request)

# @api_view(['GET'])

# @csrf_exempt
#view to get all categories
def getCategories(request):
    categories = Category.objects.all()
    return_list = []
    for item in categories:
        return_list.append(item.to_dict())
    return JsonResponse({
        'categories': return_list
    })


    return Response(serializer.data)
    
# @api_view(['POST'])

# @csrf_exempt
#view to add a category
def addCategory(request):
    POST = json.loads(request.body)

    new_category = Category.objects.create(
            category = POST['category'],
            categoryImg = POST['categoryImg'],
            createdAt = POST['createdAt'],
        )


    return getCategories(request)



# @csrf_exempt
#view to edit a category
def editCategory(request):
   EDIT = json.loads(request.body)
   Category.objects.filter(id= EDIT['id'] ).update(category = EDIT['category'], categoryImg = EDIT['categoryImg'])
   return getCategories(request)



# @csrf_exempt
#view to delete a category
def deleteCategory(request):
     DELETE = json.loads(request.body)
     category = Category.objects.get(id=DELETE['id'])
     category.delete()
     return getCategories(request)


# @csrf_exempt
#view to only get favourited categories by user id
def getFavouriteCategories(request,id):
    print(id)
    favouriteCategories = FavouriteCategory.objects.filter(user_fk = id)
    return_list = []
    for item in favouriteCategories:
        return_list.append(item.to_dict())
    print(return_list)
    return JsonResponse({
        'favouriteCategories': return_list
    })

# @csrf_exempt
#view to only get favourited categories by user id as a dictionary intstead of json response
def getFavouriteCategories_dictResponse(request,id):
    print(id)
    favouriteCategories = FavouriteCategory.objects.filter(user_fk = id)
    return_list = []
    for item in favouriteCategories:
        return_list.append(item.to_dict())
    print(return_list)
    return return_list
    
# @csrf_exempt
#view to favourite a category
def addFavouriteCategory(request):
    print("dfghjkl")
    POST = json.loads(request.body)

    new_category = FavouriteCategory.objects.create(
            user_fk = User.objects.get(id = POST['user_fk']),
            category_fk = Category.objects.get(id = POST['category_fk']['id']),
            createdAt = POST['createdAt'],
        )


    return getFavouriteCategories(request, POST['user_fk'])



# @csrf_exempt
#view to unfavourite a category
def removeFavouriteCategory(request):
     DELETE = json.loads(request.body)
     category = FavouriteCategory.objects.get(id=DELETE['id'])
     category.delete()
     return getFavouriteCategories(request, DELETE['user_fk'])

# @csrf_exempt
#view to get all articles
def getArticles(request):
    print('in method')
    articles = Article.objects.all()
    return_list = []
    for item in articles:
        return_list.append(item.to_dict())
    return JsonResponse({
        'articles': return_list
    })

# @csrf_exempt
#view to get article only in favourited categories
def getFavoriteArticles(request,id):
    print(id)
    FavouriteCategoies = getFavouriteCategories_dictResponse(request, id)
    print("",FavouriteCategoies)
    
    return_list = []
    if(len(FavouriteCategoies) > 0):
        for category in FavouriteCategoies:
            print("",category)
            # return_list.append(category)
            articles = Article.objects.filter(category_fk = category['category_fk'])
            for item in articles:
                return_list.append(item.to_dict())
        return JsonResponse({
            'articles': return_list
        })
    else:
        # articles = Article.objects.all()
        # return_list = []
        return getArticles(request)
    
    

# @csrf_exempt
#view to add a article
def addArticle(request):
    POST = json.loads(request.body)

    new_article = Article.objects.create(
            category = POST['category'],
            title = POST['title'],
            email = POST['email'],
            dob = POST['dob'],
            profileImg = POST['profileImg'],
            createdAt = POST['createdAt'],
        )


    return getArticles(request)



# @csrf_exempt
#view to get all article comments
def getArticleComments(request, article_id):
    print(article_id)
    articleComments = ArticleComment.objects.filter(article_fk = article_id)
    return_list = []
    for item in articleComments:
        return_list.append(item.to_dict())
    return JsonResponse({
        'articleComments': return_list
    })
    

# @csrf_exempt
#view to add a comment to an article 
def addArticleComment(request):
    print("fghjk")
    POST = json.loads(request.body)
    print(POST)
    # print('ArticleComment', ArticleComment.objects.filter(article_fk = POST['article_fk']['id']))
    # print('ArticleComment', POST['article_fk']['id'])
    new_category = ArticleComment.objects.create(
            article_fk = Article.objects.get(id = POST['article_fk']['id']),
            user_fk = User.objects.get(id = POST['user_fk']),
            comment = POST['comment'],
            createdAt = POST['createdAt'],
        )


    return getArticleComments(request, POST['article_fk']['id'])
    # return 'jk'


# @csrf_exempt
#view to edit a comment the user has made on an article 
def editArticleComment(request):
   EDIT = json.loads(request.body)
   ArticleComment.objects.filter(id= EDIT['id'] ).update(comment = EDIT['comment'])
   return getArticleComments(request, EDIT['article_id'] )


# @csrf_exempt
#view to delete a comment to an article 
def deleteArticleComment(request,comment_id, article_id):
     comment = ArticleComment.objects.get(id= comment_id)
     comment.delete()
     return getArticleComments(request,article_id)


# @csrf_exempt
#view to get replys of a comment to an article 
def getCommentReplys(request,comment_id):
    commentReplys = CommentReply.objects.filter(comment_fk = comment_id)
    return_list = []
    for item in commentReplys:
        return_list.append(item.to_dict())
    return JsonResponse({
        'commentReplys': return_list
    })
    

# @csrf_exempt
#view to reply to a comment on an article 
def addCommentReply(request):
    print("blakk")
    POST = json.loads(request.body)

    new_category = CommentReply.objects.create(
            comment_fk = ArticleComment.objects.get(id = POST['comment_fk']['id']),
            user_fk = User.objects.get(id = POST['user_fk']['id']),
            comment = POST['comment'],
            # createdAt = POST['createdAt'],
        )


    return getCommentReplys(request, POST['comment_fk']['id'])


# @csrf_exempt
#view to edit a reply the user has made on an comment 
def editCommentReply(request):
   EDIT = json.loads(request.body)
   CommentReply.objects.filter(id= EDIT['id'] ).update(comment_fk = EDIT['comment_fk'], user_fk = EDIT['user_fk'], comment = EDIT['comment'])
   return getCommentReplys(request)


# @csrf_exempt
#view to delete a reply the user has made on an comment 
def deleteCommentReply(request):
     DELETE = json.loads(request.body)
     article = CommentReply.objects.get(id=DELETE['id'])
     article.delete()
     return getCommentReplys(request)
