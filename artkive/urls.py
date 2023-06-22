from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from artkiveapi.views import register_user, login_user
from artkiveapi.views.imageview import ImageView
from artkiveapi.views.folderview import FolderView
from artkiveapi.views.muserview import MuserView
from artkiveapi.views.tagview import TagView
from artkiveapi.views.imagefolderview import ImageFolderView
from artkiveapi.views.imagetagview import ImageTagView


router = DefaultRouter()
router.register(r'profile', MuserView, basename='profile')
router.register(r'images', ImageView, basename='images')
router.register(r'folders', FolderView, basename='folders')
router.register(r'tags', TagView, basename='tags')
router.register(r'image_tags', ImageTagView, basename='image_tags')
router.register(r'image_folder', ImageFolderView, basename='image_folder')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
