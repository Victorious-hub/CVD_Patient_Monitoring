from typing import Iterable
from django.db import transaction
from django.shortcuts import get_object_or_404

from apps.users.models import (
    DoctorProfile,
    PatientCard,
    PatientProfile
)


@transaction.atomic
def patient_list() -> Iterable[PatientProfile]:
    patients = PatientProfile.objects.all()
    return patients


@transaction.atomic
def doctor_list() -> Iterable[DoctorProfile]:
    doctors = DoctorProfile.objects.all()
    return doctors


@transaction.atomic
def patient_get(*, slug: str) -> PatientProfile:
    patients = PatientProfile.objects.all()
    patient = get_object_or_404(patients, slug=slug)
    return patient


@transaction.atomic
def doctor_get(*, slug: str) -> PatientProfile:
    doctors = DoctorProfile.objects.all()
    doctor = get_object_or_404(doctors, slug=slug)
    return doctor


@transaction.atomic
def card_list() -> Iterable[PatientCard]:
    cards = PatientCard.objects.all()
    return cards
