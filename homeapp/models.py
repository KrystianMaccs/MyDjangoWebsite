from django.db import models

# Create your models here.
class Krystian(models.Model):
    cv = models.FilePathField()

class Contact(models.Model):
    form = models.CharField(max_length=200)

