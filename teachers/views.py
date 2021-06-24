from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # noqa

from teachers.forms import TeachersCreateForm, TeachersUpdateForm
from teachers.models import Teachers

from webargs import fields
from webargs.djangoparser import use_args


# Create your views here.
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
def get_teachers(request, args):

    teachers = Teachers.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            teachers = teachers.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='teachers/list.html',
        context={'teachers': teachers}
    )


def create_teacher(request):

    if request.method == 'GET':

        form = TeachersCreateForm()

    elif request.method == 'POST':

        form = TeachersCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    return render(
            request=request,
            template_name='teachers/create.html',
            context={'form': form}
        )


def update_teacher(request, pk):

    teacher = Teachers.objects.get(id=pk)

    if request.method == 'GET':

        form = TeachersUpdateForm(instance=teacher)

    elif request.method == 'POST':

        form = TeachersCreateForm(
            instance=teacher,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    return render(
        request=request,
        template_name='teachers/update.html',
        context={'form': form}
    )
