from django.http import HttpResponse
from django.shortcuts import render

from emp_app.models import Employee, EmployeeDepartment, EmployeeRole

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps= Employee.objects.all()
    context={
        'emps':emps
    }
    #print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method =='POST':
        emp_name=request.POST['emp_name']  
        emp_address=request.POST['emp_address']
        emp_contact_number=request.POST['emp_contact_number']
        emp_department=int(request.POST['emp_department'])
        emp_role=int(request.POST['emp_role'])
       
        #print(emp_name,emp_contact_number);

        new_emp=Employee(emp_name=emp_name,emp_address=emp_address,emp_contact_number=emp_contact_number,emp_department_id=emp_department,emp_role_id=emp_role)
        new_emp.save()
        return HttpResponse("Employe Added Succesfulll") 
        
    
    elif request.method=='GET':
        empsroles= EmployeeRole.objects.all()
        empsdepts= EmployeeDepartment.objects.all()
        
        emprolecontext={
        'empsroles':empsroles,
        'empsdepts':empsdepts
        }
        
        return render(request,'add_emp.html',emprolecontext)

    else:
        return HttpResponse("An Error Has Occured")





def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Succesfully")
        except:
            return HttpResponse("Please Choose Valid Employee")
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    return render(request,'remove_emp.html',context)





def filter_emp(request):
    return render(request,'filter_emp.html')
