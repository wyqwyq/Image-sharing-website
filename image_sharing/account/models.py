from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name = "出生日期")
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, verbose_name = "头像")
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
        
    class Meta:
        verbose_name = '简档'
        verbose_name_plural = verbose_name
        

