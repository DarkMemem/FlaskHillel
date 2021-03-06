from teachers.views import get_teachers, create_teacher, update_teacher
from django.urls import path

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:pk>/', update_teacher, name='update'),
]
