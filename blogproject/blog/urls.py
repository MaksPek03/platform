from django.urls import include, path
from blog import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new/', views.newPost, name='newPost'),
    path('uwagi/', views.uwagi_list, name='uwagi_list'),
    path('uwagi/new/', views.new_uwaga, name='new'),
    path('', views.startpage, name='startpage'),
    path('uwagi/<int:pk>/', views.uwagi_detail, name = 'uwagi_detail'),
    path('post/<int:pk>/edit/', views.edit_post, name = 'edit_post'),
    path("uwagi/<int:pk>/edit", views.edit_uwaga, name='edit_uwaga'),
    path('uwagi/<int:pk>/delete/', views.delete_uwaga, name='delete_uwaga'), 
    path('post/<int:pk>/delete', views.delete_post, name='delete_post')

]
