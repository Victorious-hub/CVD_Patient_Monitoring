from django.db import transaction
from apps.investigations.models import BloodInvestigation, CholesterolInvestigtion
from apps.users.exceptions import DoctorNotFound, PatientNotFound
from apps.users.models import PatientCard, PatientProfile


@transaction.atomic
def blood_invest_create(*,
                        slug: str,
                        hemoglobin: float,
                        white_blood_cells: float,
                        red_blood_cells: float,
                        platelets: float,
                        patient_blood_test: int,
                        comment: str,
                        ) -> BloodInvestigation:
    if not PatientCard.objects.filter(doctor_owners__slug=slug).exists():
        raise DoctorNotFound

    if not PatientCard.objects.filter(patient__id=patient_blood_test).exists():
        raise PatientNotFound

    curr_patient = PatientProfile.objects.get(id=patient_blood_test)

    blood_test = BloodInvestigation.objects.create(
        hemoglobin=hemoglobin,
        white_blood_cells=white_blood_cells,
        red_blood_cells=red_blood_cells,
        platelets=platelets,
        patient_blood_test=curr_patient,
        comment=comment,
    )

    blood_test.full_clean()
    blood_test.save()

    return blood_test


@transaction.atomic
def cholesterol_invest_create(*,
                              slug: str,
                              total_cholesterol: float,
                              hdl_cholesterol: float,
                              ldl_cholesterol: float,
                              triglycerides: float,
                              patient_chol_test: int,
                              comment: str,
                              ) -> CholesterolInvestigtion:
    if not PatientCard.objects.filter(doctor_owners__slug=slug).exists():
        raise DoctorNotFound

    if not PatientCard.objects.filter(patient__id=patient_chol_test).exists():
        raise PatientNotFound

    curr_patient = PatientProfile.objects.get(id=patient_chol_test)

    cholesterol_test = CholesterolInvestigtion.objects.create(
        total_cholesterol=total_cholesterol,
        hdl_cholesterol=hdl_cholesterol,
        ldl_cholesterol=ldl_cholesterol,
        triglycerides=triglycerides,
        patient_chol_test=curr_patient,
        comment=comment,
    )

    cholesterol_test.full_clean()
    cholesterol_test.save()

    return cholesterol_test
