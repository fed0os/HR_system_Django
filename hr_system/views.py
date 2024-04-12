import logging

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from hr_system.forms import *
from .models import *


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


class EmployeeMain(ListView):
    model = Employee
    paginate_by = 4
    template_name = 'employees/employees.html'
    context_object_name = 'employees'
    extra_context = {'title': 'Employees'}

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Employee.objects.filter(user=self.request.user)
        else:
            return Employee.objects.all()



class EmployeeCreate(CreateView):
    model = Employee
    form_class = AddEmployeeForm
    success_url = reverse_lazy('employee_list')
    template_name = 'employees/add_employee.html'

    def get_form_kwargs(self):
        kwargs = super(EmployeeCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            response = super(EmployeeCreate, self).form_valid(form)
            messages.success(self.request, 'The employee has been added!')
        else:
            messages.warning(self.request, 'You need to be logged in to add a department.')
            response = super().form_invalid(form)

        return response

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['phone', 'address', 'department']
    template_name = 'employees/employee_update.html'
    success_url = reverse_lazy('employee_list')

    def form_valid(self, form):
        messages.success(self.request, 'The employee data has been updated!')
        return super(EmployeeUpdate, self).form_valid(form)


class EmployeeDelete(DeleteView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employees/employee_delete.html'

    success_url = reverse_lazy('employee_list')

    def form_valid(self, form):
        messages.success(self.request, 'The employee has been deleted!')
        return super(EmployeeDelete, self).form_valid(form)


class DepartmentMain(ListView):
    model = Department
    # paginate_by = 2
    template_name = 'departments/departments.html'
    context_object_name = 'departments'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Department.objects.filter(user=self.request.user)
        else:
            return Department.objects.all()


    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     messages.success(self.request, 'The job has been added!')
    #     response = super(JobCreate, self).form_valid(form)
    #     logging.info(f"Job created: {form.instance.title}, User: {form.instance.user}")
    #     return response

class DepartmentCreate(CreateView):
    model = Department
    form_class = AddDepartmentForm
    success_url = reverse_lazy('departments')
    template_name = 'departments/add_department.html'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            response = super(DepartmentCreate, self).form_valid(form)
            messages.success(self.request, 'The department has been added!')
        else:
            messages.warning(self.request, 'You need to be logged in to add a department.')
            response = super().form_invalid(form)

        return response

class DepartmentUpdate(UpdateView):
    model = Department
    fields = ['name', 'description']
    template_name = 'departments/department_update.html'
    success_url = reverse_lazy('departments')

    def form_valid(self, form):
        messages.success(self.request, 'The employee data has been updated!')
        return super(DepartmentUpdate, self).form_valid(form)


class DepartmentDelete(DeleteView):
    model = Department
    context_object_name = 'department'
    template_name = 'departments/department_delete.html'

    success_url = reverse_lazy('departments')

    def form_valid(self, form):
        messages.success(self.request, 'The employee has been deleted!')
        return super(DepartmentDelete, self).form_valid(form)






class JobMain(ListView):
    model = Job
    # paginate_by = 2
    template_name = 'jobs/jobs.html'
    context_object_name = 'jobs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['jobs'] = Job.objects.filter(user=user)
        context['assignments'] = Assignment.objects.filter(user=user)
        return context


class JobCreate(CreateView):
    model = Job
    form_class = AddJobForm
    success_url = reverse_lazy('jobs')
    template_name = 'jobs/add_job.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'The job has been added!')
        response = super(JobCreate, self).form_valid(form)
        logging.info(f"Job created: {form.instance.title}")
        return response


class JobDelete(DeleteView):
    model = Job
    context_object_name = 'job'
    template_name = 'jobs/delete_job.html'

    success_url = reverse_lazy('jobs')

    def form_valid(self, form):
        messages.success(self.request, 'The job has been deleted!')
        return super(JobDelete, self).form_valid(form)


def compensations(request):
    return render(request, 'compensations.html')


def assignments(request):
    context = {
        'assignments': Assignment.objects.all()
    }
    return render(request, 'assignments/assignments.html', context)


class AssignmentMain(ListView):
    model = Assignment
    template_name = 'assignments/assignments.html'
    context_object_name = 'assignments'

    def get_queryset(self):
        user = self.request.user
        return Assignment.objects.filter(user=user)

class AssignmentCreate(CreateView):
    model = Assignment
    form_class = AddAssignmentsForm
    success_url = reverse_lazy('assignments')
    template_name = 'assignments/add_assignments.html'

    def get_form_kwargs(self):
        kwargs = super(AssignmentCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'The assignment has been added!')
        return super(AssignmentCreate, self).form_valid(form)



class AssignmentUpdate(UpdateView):
    model = Assignment
    fields = ['position', 'begin_date', 'end_date']
    template_name = 'assignments/assignment_update.html'
    success_url = reverse_lazy('assignments')

    def form_valid(self, form):
        messages.success(self.request, 'The assignment data has been updated!')
        return super(AssignmentUpdate, self).form_valid(form)


class AssignmentDelete(DeleteView):
    model = Assignment
    context_object_name = 'assignment'
    template_name = 'assignments/delete_assignment.html'

    success_url = reverse_lazy('assignments')

    def form_valid(self, form):
        messages.success(self.request, 'The job assignment been deleted!')
        return super(AssignmentDelete, self).form_valid(form)

class RegisterUser(CreateView):
    template_name = "user/register.html"
    form_class = RegistrationUserForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homepage')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


def logout_user(request):
    logout(request)
    return redirect('login')
