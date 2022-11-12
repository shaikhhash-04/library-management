from django.shortcuts import render,redirect
from app.models import Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app.forms import registerform
from django.contrib.auth.models import User

#from .forms import CreateUserForm


# Create your views here.
def login (request):
    if request.method=='POST':
        af=AuthenticationForm(request=request,data=request.POST)
        if af.is_valid():
            uname=af.cleaned_data['username']
            upass=af.cleaned_data['password']
            is_authenticate=authenticate(username=uname,password=upass)
            if is_authenticate:
                login(request,is_authenticate)
                messages.success(request,"login success")
            return redirect ('/data/')

        else:
            messages.error(request,"login failed")
            return redirect("/")

    else:
        f=AuthenticationForm()
        content={}
        content['form']=f
        return render(request,"registration/login.html",content)

def registerPage(request):
    form = registerform()

    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            form.save()

    content = {'form':form}
    return render(request,'registration/register.html',content)
    
    """if request.method=='POST':
        data=registerform(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request,' sucessfully done !!!')
            return redirect('/')
        else:
            messages.error(request,' ERROR , FILL CORRECT DETAILS !!!')
            return redirect('/register/')
    else :
        f=registerform()
        content={'form':f}
        return render(request,'app/register.html', content)"""


def userlogout(request):
    logout(request)
    return redirect("/app/login/")

def form(request):
    if (request.method=="POST"):
        name_ = request.POST['name']
        author_ = request.POST['author']
        price_ = request.POST['price']
        type_ = request.POST['type']

        print(name_)
        print(author_)
        print(price_)
        print(type_)

        insert_data = Task.objects.create(name=name_,author=author_,price=price_,type=type_)
        insert_data.save()
        return redirect("/")
    else:
        return render(request, 'app/form.html')
@login_required
def data(request):
    datas=Task.objects.all()
    return render(request, 'app/data.html', {'datas':datas})

def alldata(self):
    datas=Task.objects.all()
    data={"datas":datas}
    return render(self,'app/data.html',context=data)

def delete(request,tid):
    record_to_be_delete = Task.objects.filter(id=tid)
    record_to_be_delete.delete()
    return redirect("/")

'''def softdelete(request,tid):
    record_tobe_deleted = Task.objects.filter(id=tid)
    record_tobe_deleted.update(is_deleted='y')
    return redirect('/')'''

def update(request,tid):
    if (request.method=="POST"):
        name_ = request.POST['name']
        author_ = request.POST['author']
        price_ = request.POST['price']
        type_ = request.POST['type']

        record_to_update = Task.objects.filter(id=tid)
        record_to_update.update(name=name_,author=author_,price=price_,type=type_)

        return redirect("/")
    else:
        content={}
        content['data']=Task.objects.get(id=tid)
        return render(request, 'app/update.html',content)

def htol(request): #price
    datas=Task.objects.order_by('-price')
    data={"datas":datas}
    return render(request,'app/data.html',context=data)

def ltoh(request):#price
    datas=Task.objects.order_by('price')
    data={"datas":datas}
    return render(request,'app/data.html',context=data)

def AtoZ(request):#book
    datas=Task.objects.order_by('name')
    data={"datas":datas}
    return render(request,'app/data.html',context=data)

def ZtoA(request):#book
    datas=Task.objects.order_by('-name')
    data={"datas":datas}
    return render(request,'app/data.html',context=data)

def catfilter(request,cat):#filter category
    content={}
    content['datas']=Task.objects.filter(type=cat)
    return render(request,'app/data.html',content)

# updated authentication
"""def registerPage(request):
     form = UserCreationForm()

     if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
     content = {'form':form }
     return render(request,'accounts/register.html',content)

def loginPage(request):
    content = {}
    return render(request,'accounts/login2.html',content)
"""
