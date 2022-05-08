from django.db import models

from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14,unique=True)