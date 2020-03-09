
from django.db import models

# Create your models here.

class Projrcts(models.Model) :
    
    image = models.ImageField(upload_to='ourprojects/images/')
    
    title = models.CharField(max_length=20)

    url = models.URLField(blank=True)

    date = models.DateField()
    
    description = models.TextField(blank=True)

    def __str__(self) :
        
        return self.title