from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # noqa
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeachersCreateForm
from teachers.html_formatters import format_records
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
    "groups_number": fields.Int(
        required=False
    )},
    location="query"
)
@csrf_exempt
def get_teachers(request, args):

    teachers = Teachers.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            teachers = teachers.filter(**{param_name: param_value})

    html_form = """
        <body>
            <form method="get">

                <label>First name:</label>
                <input type="text" name="first_name"><br><br>

                <label>Last name:</label>
                <input type="text" name="last_name"><br><br>

                <label>Age:</label>
                <input type="number" name="age"><br><br>

                <label>Address:</label>
                <input type="text" name="address"><br><br>

                <label>Email:</label>
                <input type="email" name="email"><br><br>

                <label>Group Number:</label>
                <input type="number" name="group_number" min=0, max=10><br><br>

                <input type="submit" value="Submit">

           </form>
        </body>
    """

    records = format_records(teachers)

    response = html_form + records

    return HttpResponse(response)


@csrf_exempt
def create_teachers(request):

    if request.method == 'GET':

        form = TeachersCreateForm()

    elif request.method == 'POST':

        form = TeachersCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    html_form = f"""
    <form method="post">
        {form.as_p()}
      <input type="submit" value="Submit">
    </form>
    """

    response = html_form

    return HttpResponse(response)
