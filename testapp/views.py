from django.shortcuts import render, redirect
from .models import Employee, Department, EmployeeSalary
from .forms import EmployeeForm, DepartmentForm, EmployeeSalaryForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"index.html")


def Employee_list(request):
    employees = Employee.objects.all()
    #return HttpResponse("Hello")
    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employee_list')
    else:
        form = EmployeeForm()
    
    return render(request, 'add_employee.html', {'form': form})

def edit_employee(request,id):
    employee = Employee.objects.get(id=id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/employee_list')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/department_list')
    else:
        form = DepartmentForm()

    return render(request, 'add_department.html', {'form': form})

def edit_department(request, id):
    department = Department.objects.get(id=id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('/department_list')
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'edit_department.html', {'form': form, 'department': department})

def delete_department(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect('/department_list')

def salary_list(request):
    salaries = EmployeeSalary.objects.all()
    return render(request, 'salary_list.html', {'salaries': salaries})

def add_salary(request):
    if request.method == 'POST':
        form = EmployeeSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/salary_list')
    else:
        form = EmployeeSalaryForm()

    return render(request, 'add_salary.html', {'form': form})

def edit_salary(request, id):
    salary = EmployeeSalary.objects.get(id=id)

    if request.method == 'POST':
        form = EmployeeSalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('/salary_list')
    else:
        form = EmployeeSalaryForm(instance=salary)

    return render(request, 'edit_salary.html', {'form': form, 'salary': salary})

def delete_salary(request, id):
    salary = EmployeeSalary.objects.get(id=id)
    salary.delete()
    return redirect('/salary_list')
