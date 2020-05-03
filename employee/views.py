from django.shortcuts import render
from django.contrib.auth import authenticate, login 
from django.contrib import messages


# Create your views here.
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                print("hello")
    #print("hello2")
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

'''def Login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['pwd']

        user= auth.authenticate(request,email=email,password=password)
        if user is not None:
            form=auth.login(request,user)
            return redirect("/show")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')

    else:
        return render(request,'login.html')'''

