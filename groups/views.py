from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # noqa
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupsCreateForm, GroupsUpdateForm
from groups.html_formatters import format_records
from groups.models import Groups

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
@csrf_exempt
def get_groups(request, args):

    groups = Groups.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            groups = groups.filter(**{param_name: param_value})

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

                <label>Phone Number:</label>
                <input type="number" name="phone_number"><br><br>

                <label>Group Number:</label>
                <input type="number" name="group_number" min=0, max=10><br><br>

                <input type="submit" value="Search">

           </form>
        </body>
    """

    records = format_records(groups)

    response = html_form + records

    return HttpResponse(response)


@csrf_exempt
def create_group(request):

    if request.method == 'GET':

        form = GroupsCreateForm()

    elif request.method == 'POST':

        form = GroupsCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    html_form = f"""
    <form method="post">
        {form.as_p()}
      <input type="submit" value="Create">
    </form>
    """

    response = html_form

    return HttpResponse(response)


@csrf_exempt
def update_group(request, pk):

    group = Groups.objects.get(id=pk)

    if request.method == 'GET':

        form = GroupsUpdateForm(instance=group)

    elif request.method == 'POST':

        form = GroupsCreateForm(
            instance=group,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    html_form = f"""
    <form method="post">
        {form.as_p()}
      <input type="submit" value="Save">
    </form>
    """

    response = html_form

    return HttpResponse(response)
