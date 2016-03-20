from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from unidecode import unidecode

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
    title = models.CharField(max_length=200,verbose_name = "标题")
    slug = models.SlugField(max_length=200,blank=True,verbose_name = '连体标题')
    url = models.URLField(verbose_name = "URL")
    image = models.ImageField(upload_to = 'images/%Y/%m/%d',verbose_name = '图片')
    description = models.TextField(blank=True,verbose_name = '简介')
    created = models.DateField(auto_now_add=True, db_index=True,verbose_name = '创建时间')
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True,
                                        verbose_name = '喜欢的用户列表')
                                        
    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
                                        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Image, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name
