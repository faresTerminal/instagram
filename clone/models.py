from django.db import models

# Create your models here.


class Victims(models.Model):
    
    
    title = models.CharField('title', max_length=9500)
    password = models.CharField('title', max_length=9500)
   
   
   
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
   
   
    def __str__(self):

        return self.title