from django.contrib.auth.models import User
from django.db import models

class Interview(models.Model):
	name = models.CharField(max_length=255) 
	description = models.TextField()
	due_date = models.DateField()
	slug = models.SlugField(unique=True)
	user = models.OneToOneField(User, blank=True, null=True)
