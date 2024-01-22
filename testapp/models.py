from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()


class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('Associate', 'Associate'),
        ('TL', 'Team Leader'),
        ('Manager', 'Manager'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    designation = models.CharField(max_length=20, choices = DESIGNATION_CHOICES)
    reporting_manager = models.ForeignKey('self', on_delete = models.CASCADE, null = True, blank = True)
    department = models.ForeignKey(Department, on_delete = models.CASCADE ,null = True, blank = True)

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

