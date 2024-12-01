from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1)
    available_times = models.JSONField()  # Store available times as a list of time slots

    def __str__(self):
        return f"{self.full_name} - {self.specialization}"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    reason = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Booked')

    def __str__(self):
        return f"Appointment with {self.doctor.full_name} for {self.patient_name}"


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
