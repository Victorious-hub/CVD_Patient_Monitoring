from django.contrib import admin
from .models import BloodInvestigation, CholesterolInvestigtion, Investigation

admin.site.register(BloodInvestigation)
admin.site.register(CholesterolInvestigtion)
admin.site.register(Investigation)
