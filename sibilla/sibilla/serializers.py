from django.contrib.auth.models import User
from sibilla.models import Document, Category, Tag, Drive
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'url', 'username', 'email', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('id', 'name')


class DriveSerializer(serializers.ModelSerializer):
  class Meta:
    model = Drive
    fields = ('id', 'name', 'drive_id')


class DocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Document
    fields = ('id', 'name', 'description', 'files',
        'categories', 'tags', 'drive')

