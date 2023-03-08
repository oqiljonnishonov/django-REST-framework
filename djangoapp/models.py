from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name=models.CharField(max_length=20,verbose_name='First_name')
    last_name=models.CharField(max_length=20,verbose_name='Last_name')
    gender=models.CharField(max_length=20,verbose_name='Gender')
    


class Movie(models.Model):
    name=models.CharField(max_length=50,verbose_name='Movie_name')
    genre=models.CharField(max_length=50,verbose_name='Genre')
    year=models.DateField(verbose_name='Relise_year')
    actor=models.ManyToManyField(Actor)
    
    def __str__(self):
        return self.name


new=Movie.actor
print(new)