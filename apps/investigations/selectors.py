from typing import Iterable
from django.db import transaction
from apps.investigations.models import BloodInvestigation, CholesterolInvestigtion


@transaction.atomic
def patient_blood_list() -> Iterable[BloodInvestigation]:
    patient_tests = BloodInvestigation.objects.all()
    return patient_tests


@transaction.atomic
def patient_cholesterol_list() -> Iterable[CholesterolInvestigtion]:
    patient_tests = CholesterolInvestigtion.objects.all()
    return patient_tests
