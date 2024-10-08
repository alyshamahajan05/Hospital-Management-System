from django.db import models

class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.IntegerField()
    special = models.CharField(max_length=100)

class Patient(models.Model):
    Name = models.CharField(max_length=100)
    Mobile = models.IntegerField(null=True)
    gender = models.CharField(max_length=20)
    address = models.TextField()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


