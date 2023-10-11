from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import AppointmentForm

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save the appointment if the form is valid
            appointment = form.save()
            # Optionally, you can perform additional actions here
            return redirect('/')  # Redirect to a success page after successful submission
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'form': form})
