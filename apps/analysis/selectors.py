from django.db import transaction
from typing import Iterable

from django.shortcuts import get_object_or_404

from apps.analysis.models import BloodAnalysis, DiseaseAnalysis
from apps.users.models import PatientCard, PatientProfile


class AnalysisSelector:
    @transaction.atomic
    def list(self) -> Iterable[BloodAnalysis]:
        patients = BloodAnalysis.objects.all()
        return patients

    @transaction.atomic
    def get(self, slug: str) -> BloodAnalysis:
        patient = get_object_or_404(PatientProfile, slug=slug)
        patient_card = get_object_or_404(PatientCard, patient=patient)
        blood_analysis = BloodAnalysis.objects.filter(patient=patient_card).order_by('id').last()
        
        return blood_analysis
    
    @transaction.atomic
    def list_disease(self) -> DiseaseAnalysis:
        patients = DiseaseAnalysis.objects.all()
        return patients