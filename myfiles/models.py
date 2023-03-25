from django.db import models

# Create your models here.

class photo(models.Model):
    photo = models.ImageField(upload_to='media')
    UTC = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'photo'
