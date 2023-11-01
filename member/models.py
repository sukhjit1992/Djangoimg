from django.db import models
from sorl.thumbnail import ImageField

class member(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=200, blank = False, null = False)
    
    def  __str__  (self):
        return self.name 