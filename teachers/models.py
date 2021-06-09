from django.db import models


# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    age = models.ImageField(default=18, null=True)
    address = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=20, null=False)
    groups_number = models.IntegerField(null=True)
