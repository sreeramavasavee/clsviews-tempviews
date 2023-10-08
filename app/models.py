from django.db import models

# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=50)
    sprincipal=models.CharField(max_length=50)
    sfee=models.IntegerField()

