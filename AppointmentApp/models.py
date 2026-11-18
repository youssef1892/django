from django.db import models
from AccountApp.models import Doctor,Patient

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "En attente"
        CONFIRMED = "CONFIRMED", "Confirmé"
        CANCELLED = "CANCELLED", "Annulé"

    reason = models.TextField()
    appointment_date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=9, choices=Status.choices,
        default=Status.PENDING
    )

    prescription = models.FileField(
        upload_to="prescriptions/", blank=True
    )
    doctor = models.ForeignKey(
        "AccountApp.Doctor", on_delete=models.CASCADE,related_name='appointments'
    )
    patient = models.ForeignKey(
        "AccountApp.Patient", on_delete=models.CASCADE,related_name='appointments'
    )
