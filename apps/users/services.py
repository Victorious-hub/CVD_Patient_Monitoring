from typing import List
import re
from django.db import transaction
from django.shortcuts import get_object_or_404

from apps.users.models import DoctorProfile, PatientCard, PatientProfile, CustomUser
from django.contrib.auth.hashers import make_password
from apps.users.exceptions import DoctorNotFound, EmailException, MobileException, \
    PasswordLengthException, PatientCardExists, PatientNotFound


@transaction.atomic
def patient_create(*,
                   user: dict,
                   address: str
                   ) -> PatientProfile:
    pattern = r'^\+\d{10}$'

    if len(user['password']) < 8:
        raise PasswordLengthException

    if CustomUser.objects.filter(email=user['email']).exists():
        raise EmailException

    if CustomUser.objects.filter(mobile=user['mobile']).exists() or not re.match(pattern, user['mobile']):
        raise MobileException

    new_user = CustomUser.objects.create(
        mobile=user['mobile'],
        email=user['email'],
        password=make_password(user['password']),
        gender=user['gender'],
        role=user['role'],
        first_name=user['first_name'],
        last_name=user['last_name'],
    )

    obj = PatientProfile.objects.create(user=new_user, address=address)
    obj.full_clean()
    obj.save()

    return obj


@transaction.atomic
def patient_update(*,
                   slug: str,
                   user: dict,
                   address: str
                   ) -> PatientProfile:
    pattern = r'^\+\d{10}$'
    patients = PatientProfile.objects.all()
    patient = get_object_or_404(patients, slug=slug)

    if CustomUser.objects.filter(email=user['email']).exists() and patient.slug != slug:
        raise EmailException

    if CustomUser.objects.filter(mobile=user['mobile']).exists() and patient.slug != slug \
            or not re.match(pattern, user['mobile']):
        raise MobileException

    curr_patient = patient.user

    curr_patient.email = user['email']
    curr_patient.mobile = user['mobile']
    curr_patient.gender = user['gender']
    curr_patient.role = user['role']
    curr_patient.first_name = user['first_name']
    curr_patient.last_name = user['last_name']
    curr_patient.save()

    patient.address = address
    patient.save()

    return patient


@transaction.atomic
def doctor_create(*,
                  user: dict,
                  spec: str
                  ) -> DoctorProfile:
    pattern = r'^\+\d{10}$'

    if len(user['password']) < 8:
        raise PasswordLengthException

    if CustomUser.objects.filter(email=user['email']).exists():
        raise EmailException

    if CustomUser.objects.filter(mobile=user['mobile']).exists() or not re.match(pattern, user['mobile']):
        raise MobileException

    new_user = CustomUser.objects.create(
        mobile=user['mobile'],
        email=user['email'],
        password=make_password(user['password']),
        gender=user['gender'],
        role=user['role'],
        first_name=user['first_name'],
        last_name=user['last_name'],
    )

    obj = DoctorProfile.objects.create(user=new_user, spec=spec)
    obj.full_clean()
    obj.save()

    return obj


@transaction.atomic
def doctor_update(*,
                  slug: str,
                  user: dict,
                  ) -> DoctorProfile:
    pattern = r'^\+\d{10}$'
    doctors = DoctorProfile.objects.all()
    doctor = get_object_or_404(doctors, slug=slug)

    if CustomUser.objects.filter(email=user['email']).exists() and doctor.slug != slug:
        raise EmailException

    if CustomUser.objects.filter(mobile=user['mobile']).exists() and doctor.slug != slug \
            or not re.match(pattern, user['mobile']):
        raise MobileException

    curr_doctor = doctor.user

    curr_doctor.email = user['email']
    curr_doctor.mobile = user['mobile']
    curr_doctor.gender = user['gender']
    curr_doctor.first_name = user['first_name']
    curr_doctor.last_name = user['last_name']
    curr_doctor.save()

    doctor.save()

    return doctor


@transaction.atomic
def doctor_patient_add(*,
                       slug: str,
                       patients: int | List[int]
                       ) -> DoctorProfile:
    doctors = DoctorProfile.objects.all()
    doctor = get_object_or_404(doctors, slug=slug)

    doctor.patients.add(*patients)  # unpacking
    doctor.save()

    return doctor


@transaction.atomic
def card_create(*,
                id: int,
                patient: int,
                height: int,
                weight: int,
                blood_type: dict,
                allergies: dict,
                ex_conditions: str,
                is_smoking: str,
                is_alcohol: str,
                age: int
                ) -> PatientCard:

    if not DoctorProfile.objects.filter(id=id).exists():
        raise DoctorNotFound

    if not PatientProfile.objects.filter(id=patient).exists():
        raise PatientNotFound

    if PatientCard.objects.filter(id=patient).exists():
        raise PatientCardExists

    curr_doctor = DoctorProfile.objects.get(id=id)
    curr_patient = PatientProfile.objects.get(id=patient)

    patient_card = PatientCard.objects.create(
        doctor_owners=curr_doctor,
        patient=curr_patient,
        height=height,
        weight=weight,
        blood_type=blood_type,
        allergies=allergies,
        ex_conditions=ex_conditions,
        is_smoking=is_smoking,
        is_alcohol=is_alcohol,
        age=age
    )

    patient_card.full_clean()
    patient_card.save()

    return patient_card
