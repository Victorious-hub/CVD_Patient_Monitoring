from apps.investigations.models import BloodInvestigation, CholesterolInvestigtion
from apps.investigations.selectors import patient_blood_list, patient_cholesterol_list
from apps.investigations.services import blood_invest_create, cholesterol_invest_create

from rest_framework import filters
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from apps.users.permissions import IsDoctor

#from apps.users.selectors import patient_list


class PatientBloodTestCreateAPI(views.APIView):
    #permission_classes = (IsDoctor,)

    class InputSerializer(serializers.ModelSerializer):
        hemoglobin = serializers.FloatField()
        white_blood_cells = serializers.FloatField()
        red_blood_cells = serializers.FloatField()
        platelets = serializers.FloatField()
        patient_blood_test = serializers.IntegerField()
        comment = serializers.CharField()

        class Meta:
            fields = '__all__'
            model = BloodInvestigation

    def post(self, request, slug):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blood_invest_create(slug=slug, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientCholesterolTestCreateAPI(views.APIView):
    #permission_classes = (IsDoctor,)

    class InputSerializer(serializers.ModelSerializer):
        total_cholesterol = serializers.FloatField()
        hdl_cholesterol = serializers.FloatField()
        ldl_cholesterol = serializers.FloatField()
        triglycerides = serializers.FloatField()
        patient_chol_test = serializers.IntegerField()
        comment = serializers.CharField()

        class Meta:
            fields = '__all__'
            model = CholesterolInvestigtion

    def post(self, request, slug):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cholesterol_invest_create(slug=slug, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientBloodTestListAPI(views.APIView):
    permission_classes = (IsDoctor,)

    class OutputSerializer(serializers.ModelSerializer):
        hemoglobin = serializers.FloatField()
        white_blood_cells = serializers.FloatField()
        red_blood_cells = serializers.FloatField()
        platelets = serializers.FloatField()
        #patient_blood_test = serializers.PrimaryKeyRelatedField(queryset=patient_list, many=False)

        class Meta:
            fields = '__all__'
            model = BloodInvestigation

    def get(self, request):
        patient_blood = patient_blood_list()
        data = self.OutputSerializer(patient_blood, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class PatientCholesterolTestListAPI(views.APIView):
    permission_classes = (IsDoctor,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient_chol_test__email']

    class OutputSerializer(serializers.ModelSerializer):
        total_cholesterol = serializers.FloatField()
        hdl_cholesterol = serializers.FloatField()
        ldl_cholesterol = serializers.FloatField()
        triglycerides = serializers.FloatField()
        #patient_chol_test = serializers.PrimaryKeyRelatedField(queryset=patient_list, many=False)

        class Meta:
            fields = '__all__'
            model = CholesterolInvestigtion

    def get(self, request):
        patient_blood = patient_cholesterol_list()
        data = self.OutputSerializer(patient_blood, many=True).data
        return Response(data, status=status.HTTP_200_OK)


# class SearchPatientBloodView(generics.ListCreateAPIView):
#     serializer_class = PatientBloodSerializer
#     search_fields = ['patient_blood_test__user__email']
#     filter_backends = (filters.SearchFilter,)
#     queryset = BloodInvestigation.objects.all()


# class SearchPatientCholesterolView(generics.ListCreateAPIView):
#     serializer_class = PatientCholesterolSerializer
#     search_fields = ['patient_chol_test__user__email']
#     filter_backends = (filters.SearchFilter,)
#     queryset = CholesterolInvestigtion.objects.all()
