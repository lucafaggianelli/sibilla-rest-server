from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=255)


class Tag(models.Model):
  name = models.CharField(max_length=255)


class Drive(models.Model):
  drive_id = models.CharField(max_length=255)
  name = models.CharField(max_length=255)


class Document(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  files = models.CharField(max_length=255, blank=True)

  categories = models.ManyToManyField(Category, blank=True)
  tags = models.ManyToManyField(Tag, blank=True)
  drive = models.ManyToManyField(Drive, blank=True)

