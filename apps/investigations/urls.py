from django.urls import path
from .apis import (
    PatientBloodTestCreateAPI,
    PatientBloodTestListAPI,
    PatientCholesterolTestCreateAPI,
    PatientCholesterolTestListAPI,
)

urlpatterns = [
    path('v1/blood/test/<str:slug>', PatientBloodTestCreateAPI.as_view(), name='crreate_blood_test'),
    path('v1/blood', PatientBloodTestListAPI.as_view(), name='blood_patient_test'),

    path('v1/cholesterol/test/<str:slug>', PatientCholesterolTestCreateAPI.as_view(), name='create_cholesterol_test'),
    path('v1/cholesterol', PatientCholesterolTestListAPI.as_view(), name='cholesterol_patient_test'),
]
