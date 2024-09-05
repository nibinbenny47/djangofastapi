from django.http import Http404
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404, redirect
from .models import department
from .forms import DepartmentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


User = get_user_model()


def department_list(request):
    departments = department.objects.all()
    return render(request,'admin/department/list.html',{'departments':departments})

def is_adminuser(user):
    user = User.objects.get(id=user.id)
    print(user.groups_id)
    print("groupid")
    group_name = Group.objects.all().filter(
                    user=user
                )
    group_name = str(group_name[0])  # convert to string
    print(group_name)
    if group_name == 'Admin':
        return True
    else:
        return False
    

#only admun users allowed to create department----------------------------------------------
@login_required(login_url='/auth/login/')
@user_passes_test(is_adminuser,login_url='/auth/login/') 
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department created successfully')

            return redirect('department_create')
    else:
        form = DepartmentForm()
    return render(request,'admin/department/create.html',{'form':form})

def department_edit(request,pk):

    dep = department.objects.filter(id=pk)
    dep = dep.first()

    if request.method == "POST":
        form = DepartmentForm(request.POST,instance=dep)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=dep)
    return render(request,'department/create.html',{'form':form})

def department_delete(request,pk):
    dep = department.objects.filter(id = pk)
    dep = dep.first()
    dep.delete()
    return redirect('department_list')
    