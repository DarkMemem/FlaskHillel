"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from groups import views as app_views_groups

from teachers import views as app_views_teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', app_views_groups.get_groups),
    path('groups/create/', app_views_groups.create_group),
    path('groups/update/<int:pk>', app_views_groups.update_group),
    path('teachers/', app_views_teachers.get_teachers),
    path('teachers/create/', app_views_teachers.create_teacher),
    path('teachers/update/<int:pk>', app_views_teachers.update_teacher),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
