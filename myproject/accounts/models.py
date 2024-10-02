from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=25, default="Чудова кава!")
    content = models.TextField(default="Неймовірна структура!")
    author = models.ForeignKey(User, models.CASCADE)
    pub_date = models.DateField(default=datetime.now)
    