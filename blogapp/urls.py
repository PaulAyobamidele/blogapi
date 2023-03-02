from django.urls import path
from . import views



urlpatterns = [
    path('', views.PostList.as_view()),
    path('<str:pk>/', views.PostDetail.as_view())
]