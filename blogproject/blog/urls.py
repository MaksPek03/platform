from django.urls import include, path
from blog import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new/', views.newPost, name='newPost'),
    path('uwagi/', views.uwagi_list, name='uwagi_list'),
    path('uwagi/new/', views.new_uwaga, name='new'),
    path('', views.startpage, name='startpage'),
    path('uwagi/<int:pk>/', views.uwagi_detail, name = 'uwagi_detail')

]
