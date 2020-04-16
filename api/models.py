from django.db import models

# Create your models here.
class Neighborhoods(models.Model):
    city = models.CharField(max_length=50)
    neighborhood_name = models.CharField(max_length=50)
    overall_score = models.IntegerField()
    walkability_score = models.DecimalField(max_digits=13, decimal_places=10) 
    groceries_score = models.DecimalField(max_digits=13, decimal_places=10)
    parks_score = models.DecimalField(max_digits=13, decimal_places=10)
    errands_score = models.DecimalField(max_digits=13, decimal_places=10) 
    restaurants_bars_score = models.DecimalField(max_digits=13, decimal_places=10) 
    shopping_score = models.DecimalField(max_digits=13, decimal_places=10) 
    entertainment_scores = models.DecimalField(max_digits=13, decimal_places=10) 
    schools_scores = models.DecimalField(max_digits=13, decimal_places=10) 
    transit_scores = models.DecimalField(max_digits=13, decimal_places=10)
    bike_scores = models.DecimalField(max_digits=13, decimal_places=10)

# class NeighborhoodCenter(models.Model):
#     city = models.CharField(max_length=50)

# class CityCenter(models.Model):
#     city = models.CharField(max_length=50)

    