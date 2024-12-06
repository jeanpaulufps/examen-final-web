from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet, basename='user_image')
router.register(r'image', views.ImageViewSet, basename='image')
router.register(r'download_image', views.DownloadImageViewSet, basename='download_image')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_images'))
]