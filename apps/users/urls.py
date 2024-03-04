from django.urls import path
from .apis import (
    CardCreateApi,
    CardListApi,
    DoctorCreateApi,
    DoctorDetailApi,
    DoctorListApi,
    DoctorUpdateApi,
    HelloWorldView,
    PatientCreateApi,
    PatientDetailApi,
    DoctorPatientAddApi,
    PatientListApi,
    PatientUpdatelApi
)

urlpatterns = [

    path('about/', HelloWorldView.as_view()),

    path('v1/registration/patient', PatientCreateApi.as_view(), name='create_patient'),
    path('v1/patients/', PatientListApi.as_view(), name='get_patient'),
    path('v1/patients/<str:slug>/get', PatientDetailApi.as_view(), name='get_patient'),
    path('v1/patients/<str:slug>/update', PatientUpdatelApi.as_view(), name='update_patient'),

    path('v1/registration/doctor', DoctorCreateApi.as_view(), name='create_doctor'),
    path('v1/doctors/', DoctorListApi.as_view(), name='get_patient'),
    path('v1/doctors/<str:slug>/get', DoctorDetailApi.as_view(), name='get_doctor'),
    path('v1/doctors/<str:slug>/update', DoctorUpdateApi.as_view(), name='update_doctor'),
    path('v1/doctors/patient/<str:slug>/update', DoctorPatientAddApi.as_view(), name='add_doctor_patient_list'),

    path('v1/patient/card/<int:pk>', CardCreateApi.as_view(), name='fill_patient_card'),
    path('v1/patient/card', CardListApi.as_view(), name='patient_cards'),
]
