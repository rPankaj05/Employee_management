from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render,redirect
from empApp.models import Emp,Feedback
from datetime import datetime
from django.contrib import messages


def homePage(request):
    emps=Emp.objects.all()
    return render(request,"index.html",{'emps':emps}) 
 
def about(request):
    return render(request,"about.html") 


def add_emp(request):
     if request.method=="POST":
          
        #data fecthing

        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
            
        #create model object and set the data

        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.working=emp_working
        e.department=emp_department

        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.save()

        return redirect("/home/")
     return render(request,'add_emp.html',{}) 

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,'update_emp.html',{'emp':emp})

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.working=emp_working
        e.department=emp_department

        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.save()

    return redirect('/home/')


def feedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Feedback(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,"feedback.html") 

