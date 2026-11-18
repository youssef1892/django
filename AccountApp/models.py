from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator


class User(AbstractUser):
    pass
class Specialty(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Doctor(User):
    specialties = models.ManyToManyField(Specialty,related_name='doctors')
    license_number = models.CharField(max_length=6, unique=True,validators=[MinLengthValidator(6), RegexValidator(r'^\d{6}$', 'License number must be exactly 6 digits.')])
    phone = models.CharField(max_length=8)
    def __str__(self):
        return self.get_full_name() or self.username
class Patient(User):

    national_id = models.CharField(max_length=8, unique=True,validators=[MinLengthValidator(8), RegexValidator(r'^\d{8}$', 'National ID must be exactly 8 digits.')])
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()
    def __str__(self):
        return self.get_full_name() or self.username


