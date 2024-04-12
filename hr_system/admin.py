from django.contrib import admin

# Register your models here.
from .models import *

models_list = (Department, Compensation, Employee, Job, Assignment)

for model in models_list:
    admin.site.register(model)
