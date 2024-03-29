from rest_framework import views
from rest_framework import serializers
from apps.analysis.models import BloodAnalysis, CholesterolAnalysis, DiseaseAnalysis, PatientCard
from apps.analysis.selectors import AnalysisSelector
from apps.analysis.services import AnalysisService
from apps.users.constansts import ALLERGIES, BLOOD_TYPE
from rest_framework.response import Response
from rest_framework import status

from apps.users.selectors import DoctorSelector, PatientSelector
from apps.users.utils import inline_serializer


class PatientBloodCreateApi(views.APIView):
    class InputSerializer(serializers.ModelSerializer):
        patient_card = serializers.PrimaryKeyRelatedField(queryset=PatientCard.objects.all(), many=False)
        glucose = serializers.FloatField()
        ap_hi = serializers.IntegerField()
        ap_lo = serializers.IntegerField()

        class Meta:
            model = BloodAnalysis
            fields = ('patient_card', 'glucose', 'ap_hi', 'ap_lo',)

    def post(self, request, slug):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = AnalysisService(**serializer.validated_data)
        patient.create_blood_analysis(slug)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientBloodListeApi(views.APIView):

    class OutputSerializer(serializers.ModelSerializer):
        patient = inline_serializer(fields={
            'patient.user.first_name': serializers.CharField(),
            'patient.user.last_name': serializers.CharField(),
            'patient.user.email': serializers.EmailField(),
        })
        glucose = serializers.FloatField()
        ap_hi = serializers.IntegerField()
        ap_lo = serializers.IntegerField()

        class Meta:
            model = BloodAnalysis
            fields = ('patient', 'glucose', 'ap_hi', 'ap_lo',)

    def get(self, request):
        patient_blood = AnalysisSelector()
        data = self.OutputSerializer(patient_blood.list(), many=True).data
        return Response(data, status=status.HTTP_200_OK)


class PatientBloodDetailApi(views.APIView):

    class OutputSerializer(serializers.ModelSerializer):
        patient = inline_serializer(fields={
            'patient.user.first_name': serializers.CharField(),
            'patient.user.last_name': serializers.CharField(),
            'patient.user.email': serializers.EmailField(),
        })
        glucose = serializers.FloatField()
        ap_hi = serializers.IntegerField()
        ap_lo = serializers.IntegerField()

        class Meta:
            model = BloodAnalysis
            fields = ('patient', 'glucose', 'ap_hi', 'ap_lo',)

    def get(self, request, slug):
        patient_blood = AnalysisSelector()
        data = self.OutputSerializer(patient_blood.get_blood_analyses(slug)).data
        return Response(data, status=status.HTTP_200_OK)


class PatientCholesterolCreateApi(views.APIView):

    class InputSerializer(serializers.ModelSerializer):
        patient_card = serializers.PrimaryKeyRelatedField(queryset=PatientCard.objects.all(), many=False)
        cholesterol = serializers.FloatField()
        hdl_cholesterol = serializers.FloatField()
        ldl_cholesterol = serializers.FloatField()
        triglycerides = serializers.FloatField()

        class Meta:
            model = CholesterolAnalysis
            fields = ('patient_card', 'cholesterol', 'hdl_cholesterol', 'ldl_cholesterol', 'triglycerides',)

    def post(self, request, slug):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = AnalysisService(**serializer.validated_data)
        patient.create_cholesterol_analysis(slug)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientCholesterolDetailApi(views.APIView):

    class OutputSerializer(serializers.ModelSerializer):
        patient = inline_serializer(fields={
            'patient.user.first_name': serializers.CharField(),
            'patient.user.last_name': serializers.CharField(),
            'patient.user.email': serializers.EmailField(),
        })
        cholesterol = serializers.FloatField()
        hdl_cholesterol = serializers.FloatField()
        ldl_cholesterol = serializers.FloatField()
        triglycerides = serializers.FloatField()

        class Meta:
            model = BloodAnalysis
            fields = ('patient', 'cholesterol', 'hdl_cholesterol', 'ldl_cholesterol', 'triglycerides',)

    def get(self, request, slug):
        patient_blood = AnalysisSelector()
        data = self.OutputSerializer(patient_blood.get_cholesterol_analyses(slug)).data
        return Response(data, status=status.HTTP_200_OK)


class CardCreateApi(views.APIView):
    # permission_classes = (IsDoctor,)

    class InputSerializer(serializers.ModelSerializer):
        patient = serializers.IntegerField()
        smoke = serializers.BooleanField()
        alcohol = serializers.BooleanField()
        blood_type = serializers.ChoiceField(choices=BLOOD_TYPE)
        allergies = serializers.ChoiceField(choices=ALLERGIES)
        abnormal_conditions = serializers.CharField()
        allergies = serializers.JSONField()
        active = serializers.BooleanField()

        class Meta:
            model = PatientCard
            fields = '__all__'

    def post(self, request, slug):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor = AnalysisService(**serializer.validated_data)
        doctor.card_create(slug=slug)
        return Response(status=status.HTTP_201_CREATED)


class CardListApi(views.APIView):
    # permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        patient = inline_serializer(fields={
            'user.first_name': serializers.CharField(),
            'user.last_name': serializers.CharField(),
            'user.email': serializers.EmailField(),
            'age': serializers.IntegerField(),
            'height': serializers.IntegerField(),
            'weight': serializers.FloatField(),
            'birthday': serializers.DateField
        })
        smoke = serializers.FloatField()
        active = serializers.FloatField()
        alcohol = serializers.FloatField()
        blood_type = serializers.ChoiceField(choices=BLOOD_TYPE)
        allergies = serializers.JSONField()
        abnormal_conditions = serializers.CharField()

        class Meta:
            model = PatientCard
            fields = '__all__'

    def get(self, request):
        patients = DoctorSelector()
        data = self.OutputSerializer(patients.card_list(), many=True).data
        return Response(data, status=status.HTTP_200_OK)


class CardDetailApi(views.APIView):

    class OutputSerializer(serializers.ModelSerializer):
        patient = inline_serializer(fields={
            'user.first_name': serializers.CharField(),
            'user.last_name': serializers.CharField(),
            'user.email': serializers.EmailField(),
            'age': serializers.IntegerField(),
            'height': serializers.IntegerField(),
            'weight': serializers.FloatField(),
            'birthday': serializers.DateField
        })
        smoke = serializers.FloatField()
        active = serializers.FloatField()
        alcohol = serializers.FloatField()
        blood_type = serializers.ChoiceField(choices=BLOOD_TYPE)
        allergies = serializers.JSONField()
        abnormal_conditions = serializers.CharField()

        class Meta:
            model = PatientCard
            fields = '__all__'

    def get(self, request, slug):
        patients = PatientSelector()
        data = self.OutputSerializer(patients.get_card(slug=slug)).data
        return Response(data, status=status.HTTP_200_OK)


class DiseaseCreateApi(views.APIView):
    class InputSerializer(serializers.ModelSerializer):
        patient_card = serializers.PrimaryKeyRelatedField(queryset=PatientCard.objects.all(), many=False)

        class Meta:
            model = DiseaseAnalysis
            fields = ('patient_card', 'anomaly',)

    def post(self, request, slug):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = AnalysisService(**serializer.validated_data)
        patient.create_disease_prediction(slug)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DiseaseDoctorDetailApi(views.APIView):
    class OutputSerializer(serializers.ModelSerializer):
        patient = inline_serializer(fields={
            'patient.user.first_name': serializers.CharField(),
            'patient.user.last_name': serializers.CharField(),
            'patient.user.email': serializers.EmailField(),
        })
        blood_analysis = inline_serializer(fields={
            'glucose': serializers.FloatField(),
            'ap_hi': serializers.IntegerField(),
            'ap_lo': serializers.IntegerField(),
        })
        cholesterol_analysis = inline_serializer(fields={
            'cholesterol': serializers.FloatField(),
            'hdl_cholesterol': serializers.FloatField(),
            'ldl_cholesterol': serializers.FloatField(),
            'triglycerides': serializers.FloatField(),
        })
        anomaly = serializers.BooleanField()

        class Meta:
            model = DiseaseAnalysis
            fields = ('patient', 'anomaly', 'blood_analysis', 'cholesterol_analysis',)

    def get(self, request, slug):
        patients = AnalysisSelector()
        data = self.OutputSerializer(patients.list_disease(slug), many=True).data
        return Response(data, status=status.HTTP_200_OK)
