from django.db import models

# Create your models here.

class EmployeeDepartment(models.Model):
    department_name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.department_name

class EmployeeRole(models.Model):
    emp_role_name=models.CharField(max_length=100,null=False) 
    
    def __str__(self):
        return self.emp_role_name

class Employee(models.Model):
    emp_name=models.CharField(max_length=100, null=False)
    emp_address=models.CharField(max_length=50)
    emp_contact_number=models.CharField(max_length=50)
    emp_role= models.ForeignKey(EmployeeRole,on_delete=models.CASCADE)
    emp_department=models.ForeignKey(EmployeeDepartment,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %(self.emp_name)