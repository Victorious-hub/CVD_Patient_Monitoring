from datetime import datetime
from typing import Iterable, List
from django.db import transaction
from django.shortcuts import get_object_or_404

from apps.users.models import (
    CustomUser,
    DoctorProfile,
    PatientCard,
    PatientProfile
)
from abc import ABC, abstractmethod

class BaseSelectorService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def get(self, slug):
        pass


class PatientSelector(BaseSelectorService):
    @transaction.atomic
    def list(self) -> Iterable[PatientProfile]:
        patients = PatientProfile.objects.all()
        return patients
    

    @transaction.atomic
    def get(self, slug: str) -> PatientProfile:
        patient = get_object_or_404(PatientProfile, slug=slug)
        return patient


class DoctorSelector(BaseSelectorService):
    @transaction.atomic
    def list(self) -> Iterable[DoctorProfile]:
        doctors = DoctorProfile.objects.all()
        return doctors


    @transaction.atomic
    def get(self, slug: str) -> PatientProfile:
        doctor = get_object_or_404(DoctorProfile, slug=slug)
        return doctor


@transaction.atomic
def card_list() -> Iterable[PatientCard]:
    cards = PatientCard.objects.all()
    return cards
