from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    driver_license = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)

class Vehicle(models.Model):
    CATEGORY_CHOICES = [
        ('Economy', 'Economy'),
        ('Luxury', 'Luxury'),
        ('SUV', 'SUV'),
    ]
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    registration_number = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)  # Available, Rented, Under Maintenance

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    reservation_status = models.CharField(max_length=50)

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)