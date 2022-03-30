
from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user=models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    facebook_id=models.URLField(blank=True, null=True)
    profile_pic=models.ImageField(upload_to='Profile_Pics', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    