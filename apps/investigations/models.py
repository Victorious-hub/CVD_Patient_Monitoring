from django.db import models
from apps.users.models import PatientCard, PatientProfile


class BloodInvestigation(models.Model):
    hemoglobin = models.FloatField(blank=True)
    white_blood_cells = models.FloatField(blank=True)
    red_blood_cells = models.FloatField(blank=True)
    platelets = models.FloatField(blank=True)
    patient_blood_test = models.ForeignKey(PatientProfile, on_delete=models.CASCADE,
                                           related_name='patient_bld_test', null=True)
    date_created = models.DateField(auto_now_add=True)
    comment = models.CharField(null=True)

    def __str__(self):
        return f"Patient {self.patient_blood_test.user.first_name} blood analysis"

    class Meta:
        verbose_name = "blood_invest"
        verbose_name_plural = "blood_invests"


class CholesterolInvestigtion(models.Model):
    patient_chol_test = models.ForeignKey(PatientProfile, on_delete=models.CASCADE,
                                          related_name='patient_chst_test', null=True)
    total_cholesterol = models.FloatField()
    hdl_cholesterol = models.FloatField()
    ldl_cholesterol = models.FloatField()
    triglycerides = models.FloatField()
    date_created = models.DateField(auto_now_add=True)
    comment = models.CharField(null=True)

    def __str__(self):
        return f"Patient {self.patient_chol_test.user.first_name} cholesterol analysis"

    class Meta:
        verbose_name = "cholesterol_invest"
        verbose_name_plural = "cholesterol_invests"


class Investigation(models.Model):
    patient_card = models.ForeignKey(PatientCard, on_delete=models.CASCADE, related_name='patients_card', null=True)
    patient_blood = models.ManyToManyField(BloodInvestigation)
    patient_cholesterol = models.ManyToManyField(CholesterolInvestigtion)
