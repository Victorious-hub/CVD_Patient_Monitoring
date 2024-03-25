from django.db import models
from apps.users.models import PatientCard

class BaseModel(models.Model):
    patient = models.ForeignKey(PatientCard, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class BloodAnalysis(BaseModel):
    glucose = models.FloatField()
    ap_hi = models.IntegerField()  # Systolic blood pressure
    ap_lo = models.IntegerField()  # Diastolic blood pressure

    def __str__(self):
        return f"Patient blood analysis: {self.patient}"

    class Meta:
        verbose_name = "blood_invest"
        verbose_name_plural = "blood_invests"

class CholesterolAnalysis(BaseModel):
    cholesterol = models.FloatField()
    hdl_cholesterol = models.FloatField()
    ldl_cholesterol = models.FloatField()
    triglycerides = models.FloatField()

    def __str__(self):
        return f"Patient cholesterol analysis: {self.patient}"

    class Meta:
        verbose_name = "cholesterol_invest"
        verbose_name_plural = "cholesterol_invests"

class DiseaseAnalysis(BaseModel):
    blood_analysis = models.ForeignKey(BloodAnalysis, on_delete=models.CASCADE)
    cholesterol_analysis = models.ForeignKey(CholesterolAnalysis, on_delete=models.CASCADE)
    anomaly = models.BooleanField(default=False)

    def __str__(self):
        return f"Patient disease analysis: {self.patient}"

    class Meta:
        verbose_name = "disease_invest"
        verbose_name_plural = "disease_invests"