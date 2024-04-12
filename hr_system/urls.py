from django.urls import path

from . import views
from .views import *





urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('employees/', EmployeeMain.as_view(), name='employee_list'),
    path('employees/add/', EmployeeCreate.as_view(), name='add_employee'),
    path('employees/update/<int:pk>/', EmployeeUpdate.as_view(), name="employee_update"),
    path('employees/delete/<int:pk>/', EmployeeDelete.as_view(), name="employee_delete"),

    path('departments/', DepartmentMain.as_view(), name='departments'),
    path('departments/add/', DepartmentCreate.as_view(), name='add_department'),
    path('departments/update/<int:pk>/', DepartmentUpdate.as_view(), name='update_departments'),
    path('departments/delete/<int:pk>/', DepartmentDelete.as_view(), name='delete_departments'),

    path('jobs/', JobMain.as_view(), name='jobs'),
    path('jobs/add/', JobCreate.as_view(), name='add_job'),
    path('job/delete/<int:pk>/', JobDelete.as_view(), name='delete_job'),

    path('compensations/', views.compensations, name='compensations'),

    path('assignments/', AssignmentMain.as_view(), name='assignments'),
    path('assignments/add/', AssignmentCreate.as_view(), name='add_assignments'),
    path('assignments/update/<int:pk>/', AssignmentUpdate.as_view(), name='update_assignment'),

    path('assignments/delete/<int:pk>/', AssignmentDelete.as_view(), name='delete_assignment'),

    path('registrstion/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]