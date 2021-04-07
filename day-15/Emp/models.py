from django.db import models

# Create your models here.

class UsrRg(models.Model):
	username=models.CharField(max_length=120)
	password=models.CharField(max_length=120)
	email=models.CharField(max_length=120)
	age=models.IntegerField(default=10)


class NewData(models.Model):
	ch = [
	('M','Male'),('F','Female')
	]
	mobile = models.IntegerField()
	gender = models.CharField(max_length=10,choices=ch)
	pid = models.OneToOneField(UsrRg,on_delete=models.CASCADE)