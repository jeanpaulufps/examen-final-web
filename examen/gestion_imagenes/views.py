from rest_framework import viewsets
from .serializers import UserSerializer, ImageSerializer, DownloadImageSerializer
from .models import Image, User, DownloadImage

# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DownloadImageViewSet(viewsets.ModelViewSet):
    queryset = DownloadImage.objects.all()
    serializer_class = DownloadImageSerializer