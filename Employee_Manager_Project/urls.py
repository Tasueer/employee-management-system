"""
URL configuration for Employee_Manager_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path('employee_list/', views.Employee_list),
    path('add_employee/', views.add_employee),
    path("edit_employee/<int:id>",views.edit_employee),
    path("delete_employee/<int:id>",views.delete_employee),
    path('department_list/', views.department_list),
    path('add_department/', views.add_department),
    path("edit_department/<int:id>",views.edit_department),
    path("delete_department/<int:id>",views.delete_department),
    path('salary_list/', views.salary_list),
    path('add_salary/', views.add_salary),
    path("edit_salary/<int:id>",views.edit_salary),
    path("delete_salary/<int:id>",views.delete_salary),
 
]
