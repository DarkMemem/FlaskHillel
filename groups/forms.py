from django.forms import ModelForm

from groups.models import Groups


class GroupsCreateForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['first_name', 'last_name', 'age', 'address', 'email', 'groups_number', ]
