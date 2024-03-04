import uuid
from django.db import models
from django.utils.text import slugify
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from apps.users.constansts import ALCO, ALLERGIES, BLOOD_TYPE, \
    GENDER, ROLES, SMOKE, SPECS


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=11, unique=True)
    role = models.CharField(max_length=255, choices=ROLES)
    gender = models.CharField(max_length=255, choices=GENDER, default='Male')
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        slug_data = self.email.split('@')[0]
        self.slug = slugify(slug_data)
        return super(CustomUser, self).save(*args, **kwargs)


class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient', null=True)
    address = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, editable=False)

    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.slug)
        return super(PatientProfile, self).save(*args, **kwargs)


class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor', null=True)
    spec = models.CharField(max_length=255, choices=SPECS)
    patients = models.ManyToManyField(PatientProfile, related_name='patients')
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, editable=False)

    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctors"

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.slug)
        return super(DoctorProfile, self).save(*args, **kwargs)


class PatientCard(models.Model):
    doctor_owners = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_owner', null=True)
    patient = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, related_name='patient_card', null=True)
    height = models.IntegerField(blank=False)
    weight = models.IntegerField(blank=False)
    age = models.IntegerField(null=True)
    is_smoking = models.CharField(choices=SMOKE, default='No')
    is_alcohol = models.CharField(choices=ALCO, default='No')
    card_id = models.UUIDField(primary_key=False,
                               default=uuid.uuid4, editable=False, unique=True)
    blood_type = models.CharField(max_length=255, choices=BLOOD_TYPE)
    allergies = models.CharField(max_length=255, choices=ALLERGIES)
    ex_conditions = models.TextField()

    def __str__(self):
        return self.patient.user.first_name

    class Meta:
        verbose_name = "card"
        verbose_name_plural = "cards"
