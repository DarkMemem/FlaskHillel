from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from teachers.forms import TeachersCreateForm, TeachersUpdateForm, TeachersFilter
from teachers.models import Teachers


def get_teachers(request):

    teachers = Teachers.objects.all()

    obj_filter = TeachersFilter(data=request.GET, queryset=teachers)

    return render(
        request=request,
        template_name='teachers/list.html',
        context={'obj_filter': obj_filter}
    )


def create_teacher(request):

    if request.method == 'GET':

        form = TeachersCreateForm()

    elif request.method == 'POST':

        form = TeachersCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
            request=request,
            template_name='teachers/create.html',
            context={'form': form}
        )


def update_teacher(request, pk):

    teacher = get_object_or_404(Teachers, id=pk)

    if request.method == 'GET':

        form = TeachersUpdateForm(instance=teacher)

    elif request.method == 'POST':

        form = TeachersCreateForm(
            instance=teacher,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/update.html',
        context={'form': form}
    )


def delete_teacher(request, pk):

    teachers = get_object_or_404(Teachers, id=pk)
    if request.method == 'POST':
        teachers.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/delete.html',
        context={
            'teacher': teachers
        }
    )
