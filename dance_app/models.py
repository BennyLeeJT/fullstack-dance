from django.db import models

# Create your models here.
class DanceGenre(models.Model):
    name = models.CharField(blank=False, max_length=255)
    
    def __str__(self):
        return self.name

class DanceClass(models.Model):
    name = models.CharField(blank=False, max_length=255)
    time = models.IntegerField(blank=False, default=0)
    location = models.CharField(blank=False, max_length=255)
    dance_genre = models.ForeignKey(DanceGenre, on_delete=models.CASCADE, related_name='dance_app')
    
    def __str__(self):
        return self.name