from django.db import models

class Vehicle(models.Model):
    car_type = models.CharField(max_length=200)
    car_name = models.CharField(max_length=200)
    car_reg = models.CharField(max_length=200)
    """
        vehicle_location = https://django-location-field.readthedocs.io/en/latest/index.html
        vehicle_speed = 

    """
    def __str__(self):
        car = "Model: {} \n Name: {} \n Reg. No: {}".format(self.car_type, self.car_name, self.car_reg)
        return car

class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    driver_id = models.IntegerField()




