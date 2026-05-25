from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=False,null=False, related_name='Userprofile_user_set')
    picture = models.ImageField(uppload_to='userprofile/', blank=True, null=True)
