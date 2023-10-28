from django.db import models
from sorl.thumbnail import ImageField

class member(models.Model):
    name = models.CharField(max_length=200, blank = False, null = False)
    img = models.ImageField()
    def  __str__  (self):
        return self.name 