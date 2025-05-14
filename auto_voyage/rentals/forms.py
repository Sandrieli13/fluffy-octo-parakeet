from django import forms
from .models import Customer, Vehicle, Reservation, MaintenanceRecord

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        # List each field if you want or just use __all__ to include every field
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'
