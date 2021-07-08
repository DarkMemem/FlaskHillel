import random
import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.validators import adult_validator # noqa


class Groups(models.Model):
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
    groups_number = models.IntegerField(null=True)
    birthdate = models.DateField(default=datetime.date.today)
    enroll_date = models.DateField(default=datetime.date.today, null=True)
    graduate_date = models.DateField(default=datetime.date.today, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.age}, {self.address}, {self.email}, {self.phone_number}," \
               f" {self.groups_number}, {self.enroll_date} "

    @staticmethod
    def generate_groups(count):
        faker = Faker("ru_Ru")
        for _ in range(count):
            gr = Groups(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                address=faker.city(),
                email=faker.email(),
                phone_number=faker.phone_number(),
                groups_number=str(random.randint(1, 10)),
                birthdate=faker.date_between(start_date='-65y', end_date='-18y'),
            )
            gr.age = relativedelta(datetime.date.today(), gr.birthdate).years
            gr.save()
