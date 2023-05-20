from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile/img', default='profile/img/default.png')
    short_desc = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
