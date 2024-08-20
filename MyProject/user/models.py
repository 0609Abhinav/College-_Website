from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=20)
    message=models.CharField(max_length=600)

    def __str__(self):
        return self.name


class category(models.Model):
    cname=models.CharField(max_length=50)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()

class profile(models.Model):
    name=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=80,primary_key=True)
    passwd=models.CharField(max_length=60)
    ppic=models.ImageField(upload_to='static/profile/',default="")
    address=models.TextField(max_length=200)

class gallery(models.Model):
    pdes=models.CharField(max_length=200)
    gpic=models.ImageField(upload_to='static/gallery',default="")
    gdate=models.DateField()


class recruiters(models.Model):
    name=models.CharField(max_length=200)
    rpic=models.ImageField(upload_to='static/recruiters',default="")
    rdate=models.DateField()

class course(models.Model):
    cname=models.CharField(max_length=200)
    cpic=models.ImageField(upload_to='static/courses',default="")
    cdate=models.DateField()
    def __str__(self):
        return self.cname

class placements(models.Model):
    name=models.CharField(max_length=100)
    pcourse=models.ForeignKey(course,on_delete=models.CASCADE)
    branch=models.CharField(max_length=80)
    cmpname=models.CharField(max_length=80)
    cmplogo=models.ImageField(upload_to="static/placement/",default="")
    city=models.CharField(max_length=100)
    pyear=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    stupic=models.ImageField(upload_to="static/studentnpic/",default="")
    pdate=models.DateField()

class fee(models.Model):
    cpic= models.ImageField(upload_to="static/fees/", default="")
    pcourse=models.ForeignKey(course,on_delete=models.CASCADE)
    branch1=models.CharField(max_length=80)
    branch2= models.CharField(max_length=80)
    branch3= models.CharField(max_length=80)
    hodname=models.CharField(max_length=80)
    seats=models.CharField(max_length=100)
    cfee=models.IntegerField()
    eligibility=models.CharField(max_length=200)
    due=models.CharField(max_length=100)
    sdate=models.DateField()
    pdate=models.DateField()

class faculty(models.Model):
    tpic=models.ImageField(upload_to="static/faculty/", default="")
    name = models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    des= models.CharField(max_length=100)

