from django.shortcuts import render
from django.http import HttpResponse
from teachers.models import Teachers
from webargs.djangoparser import use_args
from webargs import fields
from teachers.html_formatters import format_records


# Create your views here.
@use_args({
    "first_name": fields.Str(
        required=False
    ),
    "last_name": fields.Str(
        required=False
    ),
    "birthdate": fields.Date(
        required=False
    )},
    location="query"
)
def get_teachers(request, args):

    teachers = Teachers.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            teachers = teachers.filter(**{param_name: param_value})

    records = format_records(teachers)

    return HttpResponse(records)
