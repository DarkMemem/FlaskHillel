from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from students.forms import StudentsUpdateForm, StudentsCreateForm, StudentsFilter
from students.models import Students


def get_students(request):

    students = Students.objects.all()

    obj_filter = StudentsFilter(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={'obj_filter': obj_filter},
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
