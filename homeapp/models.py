
from django.conf import settings
from django.db import models

    
    
class SchoolClass(models.Model):
    name= models.CharField(max_length=150)
    instructor =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


class School(models.Model):
    name=models.CharField(max_length=150)
    school_class= models.ManyToMany(SchoolClass)
    
    
    def __str__(self):
        return self.name
