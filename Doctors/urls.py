from django.urls import path
from . import views

urlpatterns = [
     path('create_appointment/', views.create_appointment),
]