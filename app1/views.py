from django.shortcuts import render,redirect
from .models import Student
from app1.forms import StudentForm

def studentInformation(request):
    stu = Student.objects.all()
    return render(request,'student.html',{'students':stu})

def insertInformation(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liststu')
    return render(request,'studentform.html',{'form':form,'action':'Add'})

def updateStudent(request,i):
    stu = Student.objects.get(id=i)
    form = StudentForm(instance = stu)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance = stu)
        if form.is_valid():
            form.save()
            return redirect('liststu')
    return render(request,'studentform.html',{'form':form,'action':'Edit'})

def deleteStudent(request,i):
    if request.method=='POST':
        stu = Student.objects.get(id=i)
        stu.delete()
        return redirect('liststu')
    return render(request,'delete.html')