from django.db import models


class Research(models.Model):
    research_title = models.CharField(max_length=200)
    research_author = models.CharField(max_length=255)


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_course = models.CharField(max_length=100)