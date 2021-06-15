from django.forms import ModelForm

from teachers.models import Teachers


class TeachersCreateForm(ModelForm):
    class Meta:
        model = Teachers
        fields = ['first_name', 'last_name', 'age', 'address', 'email', 'groups_number', ]
