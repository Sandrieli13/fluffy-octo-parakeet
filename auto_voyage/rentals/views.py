from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Vehicle, Reservation, MaintenanceRecord
from .forms import CustomerForm, VehicleForm, ReservationForm, MaintenanceRecordForm


def home(request):
    
    return render(request, 'rentals/home.html')

# -------------------------
# CUSTOMER VIEWS
# -------------------------

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'rentals/customer_list.html', {'customers': customers})

def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'rentals/add_customer.html', {'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'rentals/edit_customer.html', {'form': form})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'rentals/delete_customer.html', {'customer': customer})

# -------------------------
# VEHICLE VIEWS
# -------------------------

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'rentals/vehicle_list.html', {'vehicles': vehicles})

def add_vehicle(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'rentals/add_vehicle.html', {'form': form})

def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'rentals/edit_vehicle.html', {'form': form})

def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'rentals/delete_vehicle.html', {'vehicle': vehicle})

# -------------------------
# RESERVATION VIEWS
# -------------------------

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'rentals/reservation_list.html', {'reservations': reservations})

def add_reservation(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('reservation_list')
    return render(request, 'rentals/add_reservation.html', {'form': form})

def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    form = ReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
        return redirect('reservation_list')
    return render(request, 'rentals/edit_reservation.html', {'form': form})

def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'rentals/delete_reservation.html', {'reservation': reservation})

# -------------------------
# MAINTENANCE VIEWS
# -------------------------

def maintenance_list(request):
    records = MaintenanceRecord.objects.all()
    return render(request, 'rentals/maintenance_list.html', {'records': records})

def add_maintenance(request):
    form = MaintenanceRecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('maintenance_list')
    return render(request, 'rentals/add_maintenance.html', {'form': form})

def edit_maintenance(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    form = MaintenanceRecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('maintenance_list')
    return render(request, 'rentals/edit_maintenance.html', {'form': form})

def delete_maintenance(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('maintenance_list')
    return render(request, 'rentals/delete_maintenance.html', {'record': record})
