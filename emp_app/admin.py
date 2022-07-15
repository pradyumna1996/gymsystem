from django.contrib import admin
from .models import Employee,EmployeeDepartment,EmployeeRole

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeDepartment)
admin.site.register(EmployeeRole)