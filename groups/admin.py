from django.contrib import admin # noqa

# Register your models here.
from groups.models import Groups

admin.site.register(Groups)
