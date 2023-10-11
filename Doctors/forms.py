from django import forms
from .models import Appointment
from .models import Department
from .models import Doctor



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'description', 'doctor', 'department', 'email', 'phone', 'appointment_date', 'message']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialist', 'description', 'department']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']                
