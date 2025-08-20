from django.urls import include, path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new/', views.newPost, name='newPost'),
    path('post/<int:post_pk>/edit/', views.edit_post, name = 'edit_post'),
    path('post/<int:post_pk>/delete', views.delete_post, name='delete_post'),
    path('', views.startpage, name='startpage'),
    path('post/<int:post_pk>/uwagi/<int:uwaga_pk>/', views.uwagi_detail, name = 'uwagi_detail'),
    path('post/<int:post_pk>/uwagi/', views.uwagi_list, name='uwagi_list'),
    path('post/<int:post_pk>/uwagi/new/', views.new_uwaga, name='new_uwaga'),
    path("post/<int:post_pk>/uwagi/<int:uwaga_pk>/edit", views.edit_uwaga, name='edit_uwaga'),
    path('post/<int:post_pk>/uwagi/<int:uwaga_pk>/delete/', views.delete_uwaga, name='delete_uwaga'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_views, name='login'),
    path('about_me/', views.about_me, name='about_me'),
    path('contact/', views.contact, name='contact'),
    path('tag/<int:tag_id>/', views.post_by_tag, name='tag_posts')

] 
