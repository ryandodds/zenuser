from django.db import models

class Interview(models.Model):
	name = models.CharField(max_length=255) 
	description = models.TextField()
	slug = models.SlugField(unique=True)
