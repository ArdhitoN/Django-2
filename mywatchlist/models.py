from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class MyWatchList(models.Model):
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators= [MinValueValidator(1) ,MaxValueValidator(5)])
    release_date = models.DateField()
    review = models.TextField()
    is_watched = models.BooleanField()




    