from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200, unique=True)

  def __str__(self):
    return f'{self.name}'
  
  class Meta:
    ordering = ['name']
    

class Car(models.Model):
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  year = models.IntegerField()
  license_plate = models.CharField(max_length=10)
  mileage = models.IntegerField()
  current_store = models.ForeignKey(Store, on_delete=models.CASCADE)
  photo_url = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.make} {self.model}, Plate: {self.license_plate}'
  
  class Meta:
    ordering = ['make', 'model']

  
class CreditCard(models.Model):
  card_number = models.BigIntegerField()
  card_type = models.CharField(max_length=20)
  card_holder = models.ForeignKey(User, on_delete=models.CASCADE)
  expiration_date = models.DateField()
  cvv = models.IntegerField()

  def __str__(self):
    return f'{self.card_holder.last_name} {self.card_type}'
  

class Rental(models.Model):
  pickup_date = models.DateTimeField()
  dropoff_date = models.DateTimeField()
  dropoff_location = models.ForeignKey(Store, on_delete=models.CASCADE)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rental_fee = models.FloatField()
  card_on_file = models.ForeignKey(CreditCard, on_delete=models.CASCADE, default=1)

  def __str__(self):
    return f'{self.user.last_name} - {self.car} - Start: {self.pickup_date}'
