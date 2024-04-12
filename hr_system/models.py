from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models import F


class Department(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Compensation(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    compensation = models.ManyToManyField(Compensation)
    salary = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:

        ordering = [F('first_name').desc(nulls_last=True)]


class Job(models.Model):
    title = models.CharField(max_length=255)
    employees = models.ManyToManyField(Employee, through='Assignment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Job, on_delete=models.CASCADE)
    begin_date = models.DateField()
    end_date = models.DateField(default=date(9999, 12, 31))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
