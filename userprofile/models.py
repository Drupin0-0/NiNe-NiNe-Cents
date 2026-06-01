from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=False,null=False, related_name='Userprofile_user_set')
    picture = models.ImageField(upload_to='userprofile/', blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'Perfil de {self.user.username}'
