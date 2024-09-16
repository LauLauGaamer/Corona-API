from django.db import models

# Create your models here.
class States(models.Model):
        id = models.CharField(primary_key=True, max_length=2)
        name = models.CharField(max_length=200)
        abbreviation = models.CharField(max_length=2)

class Districts(models.Model):
        id = models.IntegerField(primary_key=True)
        state = models.ForeignKey(States, on_delete=models.PROTECT)
        county = models.CharField(max_length=200)
        name = models.CharField(max_length=200)

class Towns(models.Model):
        name = models.CharField(max_length=200)
        plz = models.CharField(max_length=10, primary_key=True)
        district = models.ForeignKey(Districts, on_delete=models.PROTECT)
        state = models.ForeignKey(States, on_delete=models.PROTECT)