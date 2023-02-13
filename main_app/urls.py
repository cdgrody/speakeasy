from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostList.as_view(), name='index'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts_detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('posts/<int:post_id>/add_favs/<int:profile_id>/',
         views.add_favs, name='add_favs'),

]
