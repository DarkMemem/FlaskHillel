from django.core.validators import ValidationError


def adult_validator(age, adult_age_limit=16):
    if age < adult_age_limit:
        raise ValidationError(f'Age should be greater than {adult_age_limit} y.o.')
