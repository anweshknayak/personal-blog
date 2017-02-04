from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField()
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	