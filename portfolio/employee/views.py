from django.shortcuts import render,redirect
from employee.models import Employee

def home(request):
    return render(request,'home.html')

def add(request):
    if request.method=="POST":
        n=request.POST['n']
        a=request.POST['a']
        ad=request.POST['ad']
        e=request.POST['e']
        i=request.FILES['i']
        m=Employee.objects.create(name=n,age=a,address=ad,email=e,image=i)
        m.save()

        # return view_menu(request)
        return redirect('view')


    return render(request,'add.html')

def view(request):
    k=Employee.objects.all()

    return render(request,'view.html',{'employee':k})


def edit(request,e):
    k=Employee.objects.get(id=e)
    if request.method == "POST":
        k.name=request.POST['n']
        k.age=request.POST['a']
        k.address=request.POST['ad']
        k.email=request.POST['e']


        if request.FILES.get('i')==None:
            k.save()
        else:
            k.image=request.FILES.get('i')
        k.save()
        return view(request)
    return render(request,'edit.html',{'employee':k})


def delete(request,e):
    k=Employee.objects.get(id=e)
    k.delete()

    return redirect('view')
