from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialist = models.CharField(max_length=255)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    appointment_date = models.DateTimeField()
    message = models.TextField()

    def _str_(self):
        return self.name

    # @staticmethod
    # def get_doctor_choices():
    #     return [(doctor.id, doctor.name) for doctor in Doctor.objects.all()]

    # @staticmethod
    # def get_department_choices():
    #     return [(department.id, department.name) for department in Department.objects.all()]
    # # Define doctor_choice and department_choice fields using choices
    # doctor_choice = models.IntegerField(choices=get_doctor_choices, blank=True, null=True)
    # department_choice = models.IntegerField(choices=get_department_choices, blank=True, null=True)
