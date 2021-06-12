from django.db import models
from faker import Faker
import random


# Create your models here.
class Groups(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(default=18, null=True)
    address = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=20, null=False)
    groups_number = models.IntegerField(null=True)

    @staticmethod
    def generate_groups(count):
        faker = Faker("ru_Ru")
        for _ in range(count):
            gr = Groups(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=str(random.randint(16, 55)),
                address=faker.address(),
                email=faker.email(),
                groups_number=str(random.randint(1, 10))
            )

            gr.save()
