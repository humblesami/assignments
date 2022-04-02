from PIL import Image
from os.path import exists
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='static/users/default.jpeg', blank=True, upload_to='profile_pics')
    education = models.TextField(max_length=1023, null=True, blank=True)
    major_subject = models.CharField(max_length=63, verbose_name="Major Subject", null=True, blank=True)
    detail = models.TextField(max_length=2047, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    
    def full_name(self):
        res = self.user.first_name + ' ' + self.user.last_name
        if res == ' ' or not res:
            res = f'user-{self.user.id}'
        return res

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.image:
            path_to_file = self.image.path
            if exists(path_to_file):
                img = Image.open(path_to_file)
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
