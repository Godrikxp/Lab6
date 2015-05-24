from django.db import models

class foo(models.Model):
	fio = models.CharField(max_length=200)
	age = models.IntegerField()
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)