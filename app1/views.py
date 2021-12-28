from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Signup,Photo
from . forms import SignupForm,LoginForm,UpdateForm,ChangepassForm
from django.contrib.auth import logout as logouts
# Create your views here.
def index(request):
    return render(request, 'index.html')
def signup(request):
    if request.method=='POST':
        f=SignupForm(request.POST or None,request.FILES or None)
        if f.is_valid():
            name=f.cleaned_data['Name']
            age=f.cleaned_data['Age']
            place=f.cleaned_data['Place']
            photo=f.cleaned_data['Photo']
            email=f.cleaned_data['Email']
            password=f.cleaned_data['Password']
            cpassword=f.cleaned_data['Confirmpassword']
            user=Signup.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"user already exists")
                return redirect('/signup')
            elif password!=cpassword:
                messages.warning(request,"password does not matches")
                return redirect('/signup')
            else:
                tab=Signup(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request,"account created successfully")
                return redirect('/')
    else:
        f=SignupForm()
    return render(request,'signup.html',{'form':f})
def login(request):
    if request.method=='POST':
        f=LoginForm(request.POST)
        if f.is_valid():
            email=f.cleaned_data['Email']
            password=f.cleaned_data['Password']
            user=Signup.objects.get(Email=email)
            if not user:
                messages.warning(request,"user does not exist")
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,"password does not matches")
                return redirect('/login')
            else:
                messages.success(request,"login successfully")
                return redirect('/home/%s' % user.id)
    else:
        f=LoginForm()
    return render(request,'login.html',{'form':f})
def home(request,id):
    user=Signup.objects.get(id=id)
    return render(request,'home.html',{'user':user})
def update(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        f=UpdateForm(request.POST or None,request.FILES or None,instance=user)
        if f.is_valid():
            name=f.cleaned_data['Name']
            age=f.cleaned_data['Age']
            place=f.cleaned_data['Place']
            photo=f.cleaned_data['Photo']
            email=f.cleaned_data['Email']
            f.save()
            messages.success(request,"updated successfully")
            return redirect('/home/%s' % user.id)
    else:
        f=UpdateForm(instance=user)
    return render(request,'update.html',{'user':user,'form':f})
def passwordchange(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        f=ChangepassForm(request.POST)
        if f.is_valid():
            oldpassword=f.cleaned_data['Oldpassword']
            newpassword=f.cleaned_data['Newpassword']
            cnewpassword=f.cleaned_data['Confirmnewpassword']
            if user.Password!=oldpassword:
                messages.warning(request,"password does not matches")
                return redirect('/passwordchange/%s' % user.id)
            elif newpassword!=cnewpassword:
                messages.success(request,"password does not matches")
                return redirect('/passwordchange/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,"password has been changed")
                return redirect('/home/%s' % user.id)
    else:
        f=ChangepassForm()
    return render(request,'password.html',{'user':user,'form':f})
def logout(request):
    logouts(request)
    messages.success(request,"logout successfully")
    return redirect('/')
def gallery(request):
    photos=Photo.objects.all()
    return render(request,'gallery.html',{'photos':photos})
def viewphoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photo.html',{'photo':photo})
