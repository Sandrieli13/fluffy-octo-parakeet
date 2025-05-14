from django.contrib import admin
from .models import Customer, Vehicle, Reservation, MaintenanceRecord

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Reservation)
admin.site.register(MaintenanceRecord)
