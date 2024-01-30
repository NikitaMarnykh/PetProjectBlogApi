from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('users', views.UserViewSet)

'''path('users/', views.UserViewSet.as_view({'get': 'list'})),
   path('users/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve'})),'''
urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
