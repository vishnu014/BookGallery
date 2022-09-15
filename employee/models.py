from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_name=models.CharField(max_length=120)
    department=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField()
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.email

# orm queries for creating new Employee

# emp=Employees(emp_name="abc",department="def",email="vishnu234@gmail.com",salary=30000,experience=4)
# emp.save()

# orm queries for listing all Employees

# employees=Employees.objects.all()

# orm queries for filtering Employees
# print all Employees whose department=hr
# employees=Employees.objects.filter(department="hr")
# employees
# To print all details
# for emp in employees:
# ...     print(emp.emp_name,emp.department,emp.experience,emp.salary)

# orm queries for listing employess whose experiece>5 year
# employees=Employees.objects.filter(experiece__gt=5)

# orm queries for listing employess whose salart>35000
#  employees=Employees.objects.filter(salary__gt=35000)

# orm queries for listing employess whose salart<35000

# employees=Employees.objects.filter(salary__lt=35000)
# >>> employees

# orm queries for listing employess whose experiece in range of 5-8
# employees=Employees.objects.filter(experience__gte=5,experience__lt=8)

# orm queries for fetching vishnu
# employee=Employees.objects.get(id=1)

