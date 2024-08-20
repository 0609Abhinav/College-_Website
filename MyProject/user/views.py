from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):

    cdata=category.objects.all().order_by('id')[0:6]

    return render(request,'user/index.html',{"data":cdata})

def about(request):
    return render(request,'user/about.html')

def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Email=request.POST.get("email","")
        Address=request.POST.get("address","")
        Mobile=request.POST.get("mobile","")
        Message=request.POST.get("msg","")
        x=contact(name=Name,email=Email,address=Address,mobile=Mobile,message=Message)
        x.save()
        status=True

    return render(request,'user/contactus.html',{'S':status})

def courses(request):
    cdata=course.objects.all()
    mydict={"g":cdata}
    return render(request,'user/courses.html',mydict)


def signup(req):
    if req.method == 'POST':
        Name = req.POST.get("name", "")
        Email = req.POST.get("email", "")
        Address = req.POST.get("address", "")
        Mobile = req.POST.get("mobile", "")
        Password = req.POST.get("passwd","")
        Picname = req.FILES['fu']
        profile(name=Name,email=Email,address=Address,mobile=Mobile,passwd=Password,ppic=Picname).save()
        return HttpResponse("<script>alert('You are Registered successfully');window.location.href='/user/signup';</script>")

    return render(req, 'user/signup.html')

def imagegallery(request):
    gdata=gallery.objects.all().order_by('-id')
    mydict={"d":gdata}
    return render(request,'user/gallery.html',mydict)

def recruitersd(request):
    rdata=recruiters.objects.all()
    mydict={"b":rdata}
    return render(request,'user/recruiters.html',mydict)

def placement(request):
    cdata=course.objects.all().order_by('-id')
    a=request.GET.get('msg')
    pdata=""
    if a is None:
        pdata=placements.objects.all()
    else:
        pdata=placements.objects.filter(pcourse=a)

    return render(request,'user/placements.html',{"course":cdata,"placement":pdata})

def fees(request):
    cdata=course.objects.all().order_by('-id')
    fdata=fee.objects.all()

    return render(request,'user/fees.html',{"course":cdata,"fee":fdata})

def facultys(request):
    rdata=faculty.objects.all()
    mydict={"b":rdata}
    return render(request,'user/faculty.html',mydict)