from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default="")
    pub_date = models.DateTimeField(default=timezone.now)
    art_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title+' | '+str(self.author) +' | '+ str(self.pub_date)


