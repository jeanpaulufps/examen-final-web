from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet, basename='user')
router.register(r'events', views.EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_events'))
]