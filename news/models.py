from django.db import models
# from django.views import generic
# from django.shortcuts import render
# from .models import Movie, Genre

# Create your models here.

class Feedback(models.Model):
    objects = models.Manager()
    content = models.CharField(max_length=2000)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=100)
class New(models.Model):
    title = models.CharField(max_length=200)
    context = models.CharField(max_length=2000)