import random

from django.db import models

from faker import Faker


# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(default=33, null=True)
    address = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=20, null=False)
    groups_number = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.age}, {self.address}, {self.email}, {self.groups_number}"

    @staticmethod
    def generate_teachers(count):
        faker = Faker("ru_Ru")
        for _ in range(count):
            th = Teachers(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=str(random.randint(30, 55)),
                address=faker.address(),
                email=faker.email(),
                groups_number=str(random.randint(1, 10))
            )

            th.save()
