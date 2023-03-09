from django.db import models
# this is to create the custom user model.
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.


class Employee(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    # on delete = models.Cascade will delete all the users related to the Foreignkey are deleted.
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    email = models.EmailField
    department = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    leave_available = models.IntegerField()

    def __str__(self):
        return self.user


class Holiday(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EmployeeLeave(models.Model):
    date = models.DateField()
    reason = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee
