from .models import Image, User, DownloadImage
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DownloadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadImage
        fields = '__all__'