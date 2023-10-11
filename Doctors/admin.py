from django.contrib import admin
from Doctors.models import Doctor, Department, Appointment

admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Appointment)
