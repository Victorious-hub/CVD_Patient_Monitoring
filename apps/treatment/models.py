from datetime import timezone
from django.db import models


class Consultation(models.Model):
    consult_date = models.DateTimeField(default=timezone.now)
    message = models.TextField()
