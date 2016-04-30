from django.contrib.auth.models import User
from sibilla.models import Document, Category, Tag, Drive
from sibilla.serializers import UserSerializer, DocumentSerializer,\
    TagSerializer, CategorySerializer, DriveSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer


class DriveViewSet(viewsets.ModelViewSet):
  queryset = Drive.objects.all()
  serializer_class = DriveSerializer


class DocumentViewSet(viewsets.ModelViewSet):
  queryset = Document.objects.all()
  serializer_class = DocumentSerializer

