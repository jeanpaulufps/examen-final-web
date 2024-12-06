from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()

router.register(r'tables', views.TableViewSet, basename='table')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_reservations'))
]