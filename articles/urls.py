from django.urls import path
from . import views # from current directory import views

app_name = 'articles' # to namespace our ulrs

urlpatterns = [
    path('', views.articleList, name = "list"), # name of url is "list"
    # ensure "create" comes before next url to not think it is a slug name
    path('create/', views.createArticle, name = "create"),
    path('My-Articles/', views.showMyArticles, name = "myArticles"),
    # url capturing; "slug" var name
    path('<slug>/', views.articleDetails, name = "details"),
]
