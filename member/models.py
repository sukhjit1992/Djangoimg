from django.db import models

class member(models.Model):
    name = models.CharField(max_length=200, blank = False, null = False)
    def  __str__  (self):
        return self.name 