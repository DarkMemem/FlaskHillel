# Generated by Django 3.2.4 on 2021-06-22 11:25

import django.core.validators
from django.db import migrations, models
import teachers.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_teachers_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='phone_number',
            field=models.CharField(default=795695943, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teachers',
            name='age',
            field=models.IntegerField(default=18, null=True, validators=[teachers.validators.adult_validator]),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='email',
            field=models.EmailField(max_length=40),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='last_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]