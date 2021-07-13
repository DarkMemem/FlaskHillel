import django_filters
from django.forms import ModelForm
from django.core.validators import ValidationError # noqa

from students.models import Students


class StudentsCreateForm(ModelForm):
    class Meta:
        model = Students
        fields = [
            'first_name',
            'last_name',
            'age',
            'address',
            'email',
            'phone_number',
            'groups_number',
            'birthdate',
            'enroll_date',
            'graduate_date'
        ]

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    @staticmethod
    def normalize_phone_number(value):
        return ''.join(c for c in value if c.isdigit() or c == '+')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result

    def clean_email(self):
        email = self.cleaned_data['email']
        result = email.lower()
        return result

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        result = self.normalize_phone_number(phone_number)
        return result


class StudentsUpdateForm(ModelForm):
    class Meta:
        model = Students
        fields = [
            'first_name',
            'last_name',
            'age',
            'address',
            'email',
            'phone_number',
            'groups_number',
            'birthdate',
            'enroll_date',
            'graduate_date'
        ]


class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Students
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
