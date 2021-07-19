from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]


class Pet(models.Model):
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=200)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submissionDate = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
