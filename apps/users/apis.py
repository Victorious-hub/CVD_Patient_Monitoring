import logging
from django.views.generic import TemplateView
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from apps.users.permissions import IsDoctor, IsPatient
from apps.users.constansts import ALCO, ALLERGIES, BLOOD_TYPE, GENDER, ROLES, SMOKE, SPECS
from apps.users.services import (
    DoctorService,
    PatientService,
)

from apps.users.selectors import (
    DoctorSelector,
    PatientSelector
)
from apps.users.tasks import add
from apps.users.utils import inline_serializer

from .models import (
    PatientCard,
    PatientProfile,
    DoctorProfile
)

logger = logging.getLogger(__name__)


class HelloWorldView(TemplateView):
    template_name = 'test.html'


class PatientCreateApi(views.APIView):
    class InputSerializer(serializers.ModelSerializer):
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'password': serializers.CharField(),
        })

        class Meta:
            model = PatientProfile
            fields = ('user',)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = PatientService(**serializer.validated_data)
        patient.create()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientUpdateDataApi(views.APIView):
    #permission_classes = (IsPatient,)

    class InputSerializer(serializers.ModelSerializer):
        weight =  serializers.FloatField(),
        height = serializers.IntegerField(),
        age = serializers.IntegerField(),
        gender = serializers.ChoiceField(choices=GENDER)
        birthday = serializers.DateField(),
        slug = serializers.CharField(),
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
        })

        class Meta:
            model = PatientProfile
            fields = ('user', 'weight', 'height', 'gender', 'age', 'birthday', 'slug',)

    def put(self, request, slug):
        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        patient_service = PatientService(**serializer.validated_data)
        patient_service.data_update(slug)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PatientUpdateContactApi(views.APIView):
    #permission_classes = (IsPatient,)

    class InputSerializer(serializers.ModelSerializer):
        user = inline_serializer(fields={
            'email': serializers.EmailField(),
        })
        mobile =  serializers.CharField()

        class Meta:
            model = PatientProfile
            fields = ('user', 'mobile',)

    def put(self, request, slug):
        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        patient = PatientService(**serializer.validated_data)
        patient.contact_update(slug)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PatientUpdatePasswordApi(views.APIView):
    pass
    # #permission_classes = (IsPatient,)

    # class InputSerializer(serializers.Serializer):
    #     password_confirm = serializers.CharField(),
    #     new_password = serializers.CharField(),
    #     user = inline_serializer(fields={
    #         'password': serializers.CharField(),
    #     })

    #     class Meta:
    #         model = PatientProfile
    #         fields = ('user', 'new_password', 'password_confirm',)

    # def put(self, request, slug):
    #     serializer = self.InputSerializer(data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     patient = PatientService(**serializer.validated_data)
    #     patient.password_update(slug)
    #     return Response(serializer.data, status=status.HTTP_200_OK)



class PatientListApi(views.APIView):
    #permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        weight =  serializers.FloatField(),
        height = serializers.IntegerField(),
        age = serializers.IntegerField(),
        gender = serializers.ChoiceField(choices=GENDER)
        birthday = serializers.DateField(),
        slug = serializers.CharField(),
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
        })

        class Meta:
            model = PatientProfile
            fields = ('user', 'weight', 'height', 'gender', 'age', 'birthday', 'slug', )

    def get(self, request):
        patients = PatientSelector() 
        data = self.OutputSerializer(patients.list(), many=True).data
        return Response(data, status=status.HTTP_200_OK)


class PatientDetailApi(views.APIView):
    #permission_classes = (IsPatient,)

    class OutputSerializer(serializers.ModelSerializer):
        weight =  serializers.FloatField(),
        height = serializers.IntegerField(),
        age = serializers.IntegerField(),
        gender = serializers.ChoiceField(choices=GENDER)
        birthday = serializers.DateField(),
        slug = serializers.CharField(),
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
        })

        class Meta:
            model = PatientProfile
            fields = ('user', 'weight', 'height', 'gender', 'age', 'birthday', 'slug',)

    def get(self, request, slug):
        patients = PatientSelector() 
        data = self.OutputSerializer(patients.get(slug=slug)).data
        return Response(data, status=status.HTTP_200_OK)


class DoctorCreateApi(views.APIView):
    class InputSerializer(serializers.ModelSerializer):
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'password': serializers.CharField(),
        })

        class Meta:
            model = DoctorProfile
            fields = ('user',)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor = DoctorService(**serializer.validated_data)
        doctor.create()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DoctorListApi(views.APIView):
    #permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        patients = serializers.PrimaryKeyRelatedField(queryset=PatientProfile.objects.all(), many=True)
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
        })

        class Meta:
            model = DoctorProfile
            fields = ('user','patients',)

    def get(self, request):
        doctors = DoctorSelector() 
        data = self.OutputSerializer(doctors.list(), many=True).data
        return Response(data, status=status.HTTP_200_OK)


class DoctorDetailApi(views.APIView):
    #permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        patients = serializers.PrimaryKeyRelatedField(queryset=PatientProfile.objects.all(), many=True)
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
        })

        class Meta:
            model = DoctorProfile
            fields = ('user', 'patients',)

    def get(self, request, slug):
        doctors = DoctorSelector() 
        data = self.OutputSerializer(doctors.get(slug=slug)).data
        return Response(data, status=status.HTTP_200_OK)


class DoctorUpdateApi(views.APIView):
    #permission_classes = (IsDoctor,)

    class InputSerializer(serializers.ModelSerializer):
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
        })

        class Meta:
            model = DoctorProfile
            fields = ('user',)

    def put(self, request, slug):
        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        doctor = DoctorService(**serializer.validated_data)
        doctor.contact_update(slug)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorPatientAddApi(views.APIView):
    # permission_classes = (IsDoctor,)

    class InputSerializer(serializers.ModelSerializer):
        patients = serializers.PrimaryKeyRelatedField(queryset=PatientProfile.objects.all(), many=True)

        class Meta:
            model = DoctorProfile
            fields = ('patients',)

    def put(self, request, slug):
        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        doctor = DoctorService(**serializer.validated_data)
        doctor.patient_list_update(slug=slug)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class CardCreateApi(views.APIView):
#     permission_classes = (IsDoctor,)

#     class InputSerializer(serializers.ModelSerializer):
#         patient = serializers.IntegerField()
#         height = serializers.CharField()
#         weight = serializers.CharField()
#         is_smoking = serializers.ChoiceField(choices=SMOKE)
#         is_alcohol = serializers.ChoiceField(choices=ALCO)
#         age = serializers.IntegerField()
#         blood_type = serializers.ChoiceField(choices=BLOOD_TYPE)
#         allergies = serializers.ChoiceField(choices=ALLERGIES)
#         ex_conditions = serializers.CharField()

#         class Meta:
#             model = PatientCard
#             fields = '__all__'

#     def post(self, request, pk):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         card_create(id=pk, **serializer.validated_data)
#         return Response(serializer, status=status.HTTP_201_CREATED)


# class CardListApi(views.APIView):
#     permission_classes = (IsDoctor,)

#     class OutputSerializer(serializers.ModelSerializer):
#         patient = serializers.PrimaryKeyRelatedField(queryset=PatientProfile.objects.all(), many=False)
#         doctor_owners = serializers.PrimaryKeyRelatedField(queryset=doctor_list, many=False)
#         height = serializers.CharField()
#         weight = serializers.CharField()
#         is_smoking = serializers.ChoiceField(choices=SMOKE)
#         is_alcohol = serializers.ChoiceField(choices=ALCO)
#         age = serializers.IntegerField()
#         blood_type = serializers.ChoiceField(choices=BLOOD_TYPE)
#         allergies = serializers.ChoiceField(choices=ALLERGIES)
#         ex_conditions = serializers.CharField()

#         class Meta:
#             model = PatientCard
#             fields = '__all__'

#     def get(self, request):
#         add.delay(2, 2)
#         add(2, 2)
#         patients = card_list()
#         data = self.OutputSerializer(patients, many=True).data
#         return Response(data, status=status.HTTP_200_OK)
