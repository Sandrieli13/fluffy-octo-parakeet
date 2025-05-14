from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete_customer'),

    # Vehicle URLs
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/add/', views.add_vehicle, name='add_vehicle'),
    path('vehicles/edit/<int:pk>/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicles/delete/<int:pk>/', views.delete_vehicle, name='delete_vehicle'),

    # Reservation URLs
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/add/', views.add_reservation, name='add_reservation'),
    path('reservations/edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('reservations/delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),

    # Maintenance URLs
    path('maintenance/', views.maintenance_list, name='maintenance_list'),
    path('maintenance/add/', views.add_maintenance, name='add_maintenance'),
    path('maintenance/edit/<int:pk>/', views.edit_maintenance, name='edit_maintenance'),
    path('maintenance/delete/<int:pk>/', views.delete_maintenance, name='delete_maintenance'),
]
