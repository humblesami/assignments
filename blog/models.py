import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from subjects.models import Subject


class Post(models.Model):
	title = models.CharField(max_length=100)
	picture = models.ImageField(null=True, blank=True, upload_to='FileImages')
	file = models.FileField(null=True, blank=True, upload_to='Files')
	content = models.TextField()
	private = models.BooleanField()
	date_posted = models.DateTimeField(default=timezone.now)
	amount = models.IntegerField(default=0)
	subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1, verbose_name="Subject")
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

        
