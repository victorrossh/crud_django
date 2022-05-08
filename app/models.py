from django.db import models
from cpf_field.models import CPFField


class Users(models.Model):
    name = models.CharField(max_length=100)
    cpf =  CPFField('cpf',unique=True)