from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blog_list, name="blog-list"),
    path("create-blog/", views.create_blog, name="create-blog"),
    path("<slug:blog_slug>/", views.blog_detail, name="blog-detail"),
    path("category/<str:topic>/", views.category_detail, name="category-detail"),
]
