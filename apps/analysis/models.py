from django.db import models
from apps.users.models import PatientProfile


class BloodAnalysis(models.Model):
    glucose = models.FloatField()
    ap_hi = models.IntegerField() # Systolic blood pressure
    ap_lo = models.IntegerField() # Diastolic blood pressure
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE,
                                           related_name='blood_test')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Patient blood analysis"

    class Meta:
        verbose_name = "blood_invest"
        verbose_name_plural = "blood_invests"


class CholesterolAnalysis(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE,
                                          related_name='cholesterol_test')
    cholesterol = models.FloatField()
    hdl_cholesterol = models.FloatField()
    ldl_cholesterol = models.FloatField()
    triglycerides = models.FloatField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Patient cholesterol analysis"

    class Meta:
        verbose_name = "cholesterol_invest"
        verbose_name_plural = "cholesterol_invests"


