from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    manufacture_year =  models.IntegerField()
    color = models.CharField(max_length=10)
    mileage = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.brand} - {self.manufacture_year} - {self.color} - {self.mileage} - {self.price}"
    
    
    
    