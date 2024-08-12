from django.db import models

# Create your models here.
class States(models.Model):
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=200)
        abbreviation = models.CharField(max_length=5)

class Districts(models.Model):
        id = models.IntegerField(primary_key=True)
        state = models.ForeignKey(States, on_delete=models.PROTECT)
        county = models.CharField(max_length=200)
        name = models.CharField(max_length=200)

class Towns(models.Model):
        name = models.CharField(max_length=200)
        plz = models.CharField(max_length=10)
        districts = models.ForeignKey(Districts, on_delete=models.PROTECT)
        states = models.ForeignKey(States, on_delete=models.PROTECT)