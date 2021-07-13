from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
