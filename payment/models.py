from django.db import models

# Create your models here.

class Payment(models.Model):
	name = models.CharField(max_length=100)
	card = models.FileField(null=True,blank=True,upload_to='Files')
	amount = models.TextField()
	# post_id = models.BooleanField()

	def __str__(self):
		return self.title
