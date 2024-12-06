from rest_framework import viewsets
from .serializers import EventSerializer, UserSerializer
from .models import Event, User

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer