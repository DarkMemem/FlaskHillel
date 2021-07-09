from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from students.forms import StudentsUpdateForm, StudentsCreateForm
from students.models import Students

from webargs import fields
from webargs.djangoparser import use_args


@use_args({
    "first_name": fields.Str(
        required=False
    ),
    "last_name": fields.Str(
        required=False
    ),
    "age": fields.Int(
        required=False
    ),
    "address": fields.Str(
        required=False
    ),
    "email": fields.Str(
        required=False
    ),
    "phone_number": fields.Int(
        required=False
    ),
    "groups_number": fields.Int(
        required=False
    )},
    location="query"
)
def get_students(request, args):

    students = Students.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            students = students.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='students/list.html',
        context={'students': students},
    )


def create_student(request):

    if request.method == 'GET':

        form = StudentsCreateForm()

    elif request.method == 'POST':

        form = StudentsCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
            request=request,
            template_name="students/create.html",
            context={'form': form},
        )


def update_student(request, pk):

    student = get_object_or_404(Students, id=pk)

    if request.method == 'GET':

        form = StudentsUpdateForm(instance=student)

    elif request.method == 'POST':

        form = StudentsUpdateForm(
            instance=student,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/update.html',
        context={'form': form},
    )


def delete_student(request, pk):
    students = get_object_or_404(Students, id=pk)
    if request.method == 'POST':
        students.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/delete.html',
        context={
            'students': students
        }
    )
