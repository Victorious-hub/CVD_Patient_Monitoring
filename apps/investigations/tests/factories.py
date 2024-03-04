import random
from apps.users.models import CustomUser, PatientProfile
import factory
import uuid
from apps.investigations.models import BloodInvestigation, CholesterolInvestigtion
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class CustomTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = 'patient@gmail.com'
    is_staff = 'True'
    first_name = factory.LazyFunction(lambda: faker.name())
    last_name = 'last_name'
    password = '12345678'
    mobile = '+1122334455'
    role = 'P'
    gender = 'Male'
    is_active = True
    is_staff = False


class CustomTestFactory1(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = 'patient_hello@gmail.com'
    is_staff = 'True'
    first_name = factory.LazyFunction(lambda: faker.name())
    last_name = 'last_name'
    password = '12345678'
    mobile = '+1234567890'
    role = 'D'
    gender = 'Male'
    is_active = True
    is_staff = False


class PatientFactoryBlood(factory.django.DjangoModelFactory):
    class Meta:
        model = PatientProfile

    user = factory.SubFactory(CustomTestFactory)
    slug = factory.LazyAttribute(lambda obj: obj.user.email.split('@')[0])
    address = factory.LazyFunction(lambda: faker.sentence(nb_words=10))


class PatientFactoryCholesterol(factory.django.DjangoModelFactory):
    class Meta:
        model = PatientProfile

    user = factory.SubFactory(CustomTestFactory1)
    slug = factory.LazyAttribute(lambda obj: obj.user.email.split('@')[0])
    address = factory.LazyFunction(lambda: faker.sentence(nb_words=10))
    

class BloodInvestigationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BloodInvestigation

    hemoglobin = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    white_blood_cells = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    red_blood_cells = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    platelets = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    patient_blood_test = factory.SubFactory(PatientFactoryBlood)
    comment = factory.LazyFunction(lambda: faker.name())


class CholesterolInvestigationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CholesterolInvestigtion

    total_cholesterol = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    hdl_cholesterol = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    ldl_cholesterol = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    triglycerides = factory.LazyAttribute(lambda x: random.randrange(0, 100))
    patient_chol_test = factory.SubFactory(PatientFactoryCholesterol)
    comment = factory.LazyFunction(lambda: faker.name())