from django.db import models

class Vehicle(models.Models):
    vehicle_type = models.CharField(max_length=200)
    vehicle_name = models.CharField(max_length=200)
    vehicle_registration = models.CharField(max_length=200)
    """
        vehicle_location = https://django-location-field.readthedocs.io/en/latest/index.html
        vehicle_speed = 

    """
    car = f"Model: {vehicle_type} \n Name: {vehicle_name} \n Reg. No: {vehicle_registration}"
    def __str__(self):
        return self.car

class Driver(models.Models):
    driver_name = models.CharField(max_length=100)
    driver_id = models.IntegerField(length=50)




