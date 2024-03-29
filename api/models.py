from django.db import models
from django.utils import timezone


# Create your models here.

class Nameken(models.Model):
    token = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=500, null=True)
    role = models.CharField(max_length=100, null=True) 
    expiry_date = models.DateField(blank=True, null=True, default=timezone.now)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name, self.token    
