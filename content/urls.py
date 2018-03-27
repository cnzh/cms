from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_view, name='post_view'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/drafts/', views.post_drafts, name='post_drafts'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

]