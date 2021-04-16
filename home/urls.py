from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name ="home"),
    path('detail/<int:id>/', views.blog_single, name="blog-single"),
    path('handle-comment/', views.handle_comment, name="handle-comment")
]