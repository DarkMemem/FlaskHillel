import random
import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.models import Group


class Students(models.Model):
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
    groups_number = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students', blank=True)
    birthdate = models.DateField(default=datetime.date.today)
    enroll_date = models.DateField(default=datetime.date.today, null=True)
    graduate_date = models.DateField(default=datetime.date.today, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.age}, {self.address}, {self.email}, {self.phone_number}," \
               f" {self.groups_number}, {self.enroll_date} "

    @staticmethod
    def generate_students(count):
        faker = Faker("ru_Ru")
        for _ in range(count):
            st = Students(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                address=faker.city(),
                email=faker.email(),
                phone_number=faker.phone_number(),
                birthdate=faker.date_between(start_date='-65y', end_date='-18y'),
            )
            st.age = relativedelta(datetime.date.today(), st.birthdate).years
            st.save()
