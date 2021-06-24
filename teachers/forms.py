from django.forms import ModelForm
from django.core.validators import ValidationError

from teachers.models import Teachers


class TeachersCreateForm(ModelForm):
    class Meta:
        model = Teachers
        fields = [
            'first_name',
            'last_name',
            'age',
            'address',
            'email',
            'phone_number',
            'groups_number',
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
        if Teachers.objects.filter(phone_number=phone_number).exclude(id=self.instance.id).exists():
            raise ValidationError("Already exist")
        result = self.normalize_phone_number(phone_number)
        return result


class TeachersUpdateForm(ModelForm):
    class Meta:
        model = Teachers
        fields = [
            'first_name',
            'last_name',
            'age',
            'address',
            'email',
            'phone_number',
            'groups_number',
        ]
