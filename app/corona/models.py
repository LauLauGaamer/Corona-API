from django.db import models

# Create your models here.
class States(models.Model):
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=200)
        abbreviation = models.CharField(max_length=5)

class County(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=200)
        state = models.ForeignKey(States, on_delete=models.PROTECT)

class Districts(models.Model):
        id = models.IntegerField(primary_key=True)
        state = models.ForeignKey(States, on_delete=models.PROTECT)
        county = models.ForeignKey(County, on_delete=models.PROTECT)
        name = models.CharField(max_length=200)
