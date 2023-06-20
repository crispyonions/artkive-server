from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from artkiveapi.views import register_user, login_user
from artkiveapi.views.imageview import ImageView
from artkiveapi.views.folderview import FolderView
from artkiveapi.views.muserview import MuserView
from artkiveapi.views.tagview import TagView


router = DefaultRouter()
router.register(r'profile', MuserView, basename='profile')
router.register(r'images', ImageView, basename='images')
router.register(r'folders', FolderView, basename='folders')
router.register(r'tags', TagView, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
