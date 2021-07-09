from django.contrib import admin # noqa

# Register your models here.
from students.models import Students

admin.site.register(Students)
