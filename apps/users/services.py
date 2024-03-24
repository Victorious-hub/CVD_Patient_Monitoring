from datetime import datetime
from typing import List
import re
from django.db import transaction
from django.shortcuts import get_object_or_404

from apps.users.models import DoctorProfile, PatientCard, PatientProfile, CustomUser
from django.contrib.auth.hashers import make_password
from apps.users.exceptions import DoctorNotFound, EmailException, MobileException, \
    PasswordLengthException, PatientCardExists, PatientNotFound


class PatientService:
    def __init__(self,
                 user: CustomUser = None,
                 weight: float = None,
                 height: int = None,
                 gender: str = None,
                 birthday: datetime = None,
                 age: int = None,
                 mobile: str = None,
                 new_password: str = None,
                 password_confirm: str = None,
                 slug: str = None,
                 ):
        self.mobile = mobile
        self.user = user
        self.weight = weight
        self.height = height
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.new_password = new_password
        self.password_confirm = password_confirm
        self.slug = slug

    @transaction.atomic
    def create(self) -> PatientProfile:

        if len(self.user['password']) < 8:
            raise PasswordLengthException

        if CustomUser.objects.filter(email=self.user['email']).exists():
            raise EmailException

        new_user = CustomUser.objects.create(
            first_name=self.user['first_name'],
            last_name=self.user['last_name'],
            password=make_password(self.user['password']),
            email=self.user['email'],
        )

        obj = PatientProfile.objects.create(user=new_user)
        obj.full_clean()
        obj.save()

        return obj

    @transaction.atomic
    def data_update(self, slug: str) -> PatientProfile:
        patient = get_object_or_404(PatientProfile, slug=slug)

        patient.age = self.age
        patient.height = self.height
        patient.weight = self.weight
        patient.gender = self.gender
        patient.birthday = self.birthday

        patient.save()

        return patient

    @transaction.atomic
    def contact_update(self, slug: str) -> PatientProfile:
        patient = get_object_or_404(PatientProfile, slug=slug)
        pattern = r'^\+\d{10}$'
        curr_patient = patient.user

        if CustomUser.objects.filter(email=self.user['email']).exists() and patient.slug != slug:
            raise EmailException

        if PatientProfile.objects.filter(mobile=self.mobile).exists() and patient.slug != slug \
                or not re.match(pattern, self.mobile):
            raise MobileException

        patient.mobile = self.mobile
        curr_patient.first_name = self.user['first_name']
        curr_patient.last_name = self.user['last_name']
        curr_patient.email = self.user['email']
        curr_patient.save()
        patient.save()

        return patient


class DoctorService:
    def __init__(self,
                 user: CustomUser = None,
                 patients: List[int] = None,
                 patient: int = None,
                 smoke: float = None,
                 alcohol: float = None,
                 abnormal_conditions: str = None,
                 allergies: dict = None,
                 blood_type: str = None,
                 active: float = None
                 ):
        self.patients = patients
        self.user = user
        self.patient = patient
        self.smoke = smoke
        self.alcohol = alcohol
        self.abnormal_conditions = abnormal_conditions
        self.allergies = allergies
        self.blood_type = blood_type
        self.active = active

    @transaction.atomic
    def create(self) -> DoctorProfile:

        if len(self.user['password']) < 8:
            raise PasswordLengthException

        if CustomUser.objects.filter(email=self.user['email']).exists():
            raise EmailException

        new_user = CustomUser.objects.create(
            email=self.user['email'],
            password=make_password(self.user['password']),
            first_name=self.user['first_name'],
            last_name=self.user['last_name'],
        )

        obj = DoctorProfile.objects.create(user=new_user)
        obj.full_clean()
        obj.save()

        return obj

    @transaction.atomic
    def contact_update(self, slug: str) -> DoctorProfile:
        doctor = get_object_or_404(DoctorProfile, slug=slug)

        if CustomUser.objects.filter(email=self.user['email']).exists() and doctor.slug != slug:
            raise EmailException

        doctor.user.email = self.user['email']
        doctor.user.save()

        return doctor

    @transaction.atomic
    def patient_list_update(self,
                            slug: str,
                            ) -> DoctorProfile:
        doctor = get_object_or_404(DoctorProfile, slug=slug)

        doctor.patients.add(*self.patients)  # unpacking
        doctor.save()

        return doctor

    @transaction.atomic
    def card_create(self,
                    slug: str,
                    ) -> PatientCard:

        if not DoctorProfile.objects.filter(slug=slug).exists():
            raise DoctorNotFound

        if not PatientProfile.objects.filter(id=self.patient).exists():
            raise PatientNotFound

        if PatientCard.objects.filter(patient=self.patient).exists():
            raise PatientCardExists

        curr_patient = PatientProfile.objects.get(id=self.patient)
        doctor = get_object_or_404(DoctorProfile, slug=slug)

        patient_card = PatientCard.objects.create(
            abnormal_conditions=self.abnormal_conditions,
            patient=curr_patient,
            allergies=self.allergies,
            smoke=self.smoke,
            alcohol=self.alcohol,
            blood_type=self.blood_type,
            active=self.active
        )

        patient_card.full_clean()
        patient_card.save()
        doctor.patient_cards.add(patient_card)

        return patient_card
