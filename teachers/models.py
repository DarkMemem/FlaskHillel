import random
import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from teachers.validators import adult_validator # noqa


class Teachers(models.Model):
    first_name = models.CharField(max_length=20, null=False, validators=[
        MinLengthValidator(2),
    ])
    last_name = models.CharField(max_length=20, null=False, validators=[
        MinLengthValidator(2)
    ])
    age = models.IntegerField(default=18, null=True)
    address = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=50, null=False)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=False)
    birthdate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.age},{self.address}, {self.email}, {self.phone_number},"

    @staticmethod
    def generate_teachers(count):
        faker = Faker("ru_Ru")
        for _ in range(count):
            th = Teachers(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                address=faker.city(),
                email=faker.email(),
                phone_number=faker.phone_number(),
                birthdate=faker.date_between(start_date='-65y', end_date='-18y'),
            )
            th.age = relativedelta(datetime.date.today(), th.birthdate).years
            th.save()
