from django.utils.translation import gettext_lazy as _

ROLES = (
    ('P', _('Patient')),
    ('D', _('Doctor')),
    ('H', _('Head')),
)

SPECS = (
    ('D', _('Dantist')),
    ('C', _('Cardio')),
)

BLOOD_TYPE = (
    ('Group I', _('I')),
    ('Group II', _('II')),
    ('Group III', _('III')),
    ('Group IV', _('IV'))
)

ALLERGIES = (
    ('Pollen', _('P')),
    ('Peanuts', _('PN')),
    ('Milk', _('M')),
    ('Tree Nut', _('TN'))
)

GENDER = (
    ('Male', _('M')),
    ('Female', _('F')),
)

SMOKE = (
    ('Yes', _('1')),
    ('No', _('0'))
)

ALCO = (
    ('Yes', _('1')),
    ('No', _('0'))
)
