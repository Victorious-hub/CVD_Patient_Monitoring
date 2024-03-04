import logging
from django.views.generic import TemplateView
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from apps.users.permissions import IsDoctor, IsPatient
from apps.users.constansts import ALCO, ALLERGIES, BLOOD_TYPE, GENDER, ROLES, SMOKE, SPECS
from apps.users.services import (
    card_create,
    doctor_create,
    doctor_patient_add,
    doctor_update,
    patient_create,
    patient_update
)

from apps.users.selectors import (
    card_list,
    doctor_get,
    doctor_list,
    patient_get,
    patient_list
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
        address = serializers.CharField()
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'mobile': serializers.CharField(),
            'password': serializers.CharField(),
            'role': serializers.ChoiceField(choices=ROLES),
            'gender': serializers.ChoiceField(choices=GENDER)
        })

        class Meta:
            model = PatientProfile
            fields = ('user', 'address',)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient_create(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientListApi(views.APIView):
    permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        address = serializers.CharField()
        id = serializers.CharField()
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'mobile': serializers.CharField(),
            'role': serializers.ChoiceField(choices=ROLES),
            'gender': serializers.ChoiceField(choices=GENDER)
        })

        class Meta:
            model = PatientProfile
            fields = ('id', 'user', 'address',)

    def get(self, request):
        patients = patient_list()
        data = self.OutputSerializer(patients, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class PatientDetailApi(views.APIView):
    permission_classes = (IsPatient,)

    class OutputSerializer(serializers.ModelSerializer):
        address = serializers.CharField()
        id = serializers.CharField()
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'slug': serializers.CharField(),
            'mobile': serializers.CharField(),
            'role': serializers.ChoiceField(choices=ROLES),
            'gender': serializers.ChoiceField(choices=GENDER)
        })

        class Meta:
            model = PatientProfile
            fields = ('id', 'user', 'address',)

    def get(self, request, slug):
        patient = patient_get(slug=slug)
        data = self.OutputSerializer(patient).data
        return Response(data, status=status.HTTP_200_OK)


class PatientUpdatelApi(views.APIView):
    permission_classes = (IsPatient,)

    class InputSerializer(serializers.ModelSerializer):
        address = serializers.CharField()
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'mobile': serializers.CharField(),
            'role': serializers.ChoiceField(choices=ROLES),
            'gender': serializers.ChoiceField(choices=GENDER)
        })

        class Meta:
            model = PatientProfile
            fields = ('user', 'address',)

    def put(self, request, slug):
        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        patient_update(slug=slug, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorCreateApi(views.APIView):
    class InputSerializer(serializers.ModelSerializer):
        spec = serializers.ChoiceField(choices=SPECS)
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'mobile': serializers.CharField(),
            'password': serializers.CharField(),
            'role': serializers.ChoiceField(choices=ROLES),
            'gender': serializers.ChoiceField(choices=GENDER)
        })

        class Meta:
            model = DoctorProfile
            fields = ('user', 'spec',)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor_create(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DoctorListApi(views.APIView):
    #permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        spec = serializers.ChoiceField(choices=SPECS)
        patients = serializers.PrimaryKeyRelatedField(queryset=patient_list, many=True)
        id = serializers.CharField()
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'slug': serializers.CharField(),
            'mobile': serializers.CharField(),
            'role': serializers.ChoiceField(choices=ROLES),
            'gender': serializers.ChoiceField(choices=GENDER)
        })

        class Meta:
            model = DoctorProfile
            fields = ('id', 'user', 'spec', 'patients',)

    def get(self, request):
        patients = doctor_list()
        data = self.OutputSerializer(patients, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class DoctorDetailApi(views.APIView):
    permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        spec = serializers.ChoiceField(choices=SPECS)
        patients = serializers.PrimaryKeyRelatedField(queryset=patient_list, many=True)
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'mobile': serializers.CharField(),
            'role': serializers.ChoiceField(choices=ROLES),
            'gender': serializers.ChoiceField(choices=GENDER)
        })

        class Meta:
            model = DoctorProfile
            fields = ('user', 'spec', 'patients',)

    def get(self, request, slug):
        doctor = doctor_get(slug=slug)
        data = self.OutputSerializer(doctor).data
        return Response(data, status=status.HTTP_200_OK)


class DoctorUpdateApi(views.APIView):
    permission_classes = (IsDoctor,)

    class InputSerializer(serializers.ModelSerializer):
        user = inline_serializer(fields={
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
            'email': serializers.EmailField(),
            'mobile': serializers.CharField(),
            'gender': serializers.ChoiceField(choices=GENDER)
        })

        class Meta:
            model = DoctorProfile
            fields = ('user',)

    def put(self, request, slug):
        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        doctor_update(slug=slug, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorPatientAddApi(views.APIView):
    permission_classes = (IsDoctor,)

    class InputSerializer(serializers.ModelSerializer):
        patients = serializers.PrimaryKeyRelatedField(queryset=PatientProfile.objects.all(), many=True)

        class Meta:
            model = DoctorProfile
            fields = ('patients',)

    def put(self, request, slug):
        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        doctor_patient_add(slug=slug, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CardCreateApi(views.APIView):
    permission_classes = (IsDoctor,)

    class InputSerializer(serializers.ModelSerializer):
        patient = serializers.IntegerField()
        height = serializers.CharField()
        weight = serializers.CharField()
        is_smoking = serializers.ChoiceField(choices=SMOKE)
        is_alcohol = serializers.ChoiceField(choices=ALCO)
        age = serializers.IntegerField()
        blood_type = serializers.ChoiceField(choices=BLOOD_TYPE)
        allergies = serializers.ChoiceField(choices=ALLERGIES)
        ex_conditions = serializers.CharField()

        class Meta:
            model = PatientCard
            fields = '__all__'

    def post(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        card_create(id=pk, **serializer.validated_data)
        return Response(serializer, status=status.HTTP_201_CREATED)


class CardListApi(views.APIView):
    permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        patient = serializers.PrimaryKeyRelatedField(queryset=PatientProfile.objects.all(), many=False)
        doctor_owners = serializers.PrimaryKeyRelatedField(queryset=doctor_list, many=False)
        height = serializers.CharField()
        weight = serializers.CharField()
        is_smoking = serializers.ChoiceField(choices=SMOKE)
        is_alcohol = serializers.ChoiceField(choices=ALCO)
        age = serializers.IntegerField()
        blood_type = serializers.ChoiceField(choices=BLOOD_TYPE)
        allergies = serializers.ChoiceField(choices=ALLERGIES)
        ex_conditions = serializers.CharField()

        class Meta:
            model = PatientCard
            fields = '__all__'

    def get(self, request):
        add.delay(2, 2)
        add(2, 2)
        patients = card_list()
        data = self.OutputSerializer(patients, many=True).data
        return Response(data, status=status.HTTP_200_OK)
