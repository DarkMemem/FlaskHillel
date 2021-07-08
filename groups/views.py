from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from groups.forms import GroupsCreateForm, GroupsUpdateForm
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
def get_groups(request, args):

    groups = Groups.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            groups = groups.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='groups/list.html',
        context={'groups': groups},
    )


def create_group(request):

    if request.method == 'GET':

        form = GroupsCreateForm()

    elif request.method == 'POST':

        form = GroupsCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
            request=request,
            template_name="groups/create.html",
            context={'form': form},
        )


def update_group(request, pk):

    group = get_object_or_404(Groups, id=pk)

    if request.method == 'GET':

        form = GroupsUpdateForm(instance=group)

    elif request.method == 'POST':

        form = GroupsCreateForm(
            instance=group,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form},
    )


def delete_group(request, pk):
    groups = get_object_or_404(Groups, id=pk)
    if request.method == 'POST':
        groups.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/delete.html',
        context={
            'groups': groups
        }
    )
