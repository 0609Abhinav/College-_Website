from django.contrib import admin

# Register your models here.
from .models import *
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','address','mobile','message')

admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpic','cdate')

admin.site.register(category,categoryAdmin)


class profileAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','email','address','ppic','passwd')
admin.site.register(profile,profileAdmin)

class galleryAdmin(admin.ModelAdmin):
    list_display = ('pdes','gpic','gdate')
admin.site.register(gallery,galleryAdmin)

class recruitersAdmin(admin.ModelAdmin):
    list_display = ('name','rpic','rdate')
admin.site.register(recruiters,recruitersAdmin)

class courseAdmin(admin.ModelAdmin):
    list_display = ('cname','cpic','cdate')
admin.site.register(course,courseAdmin)

class placementsAdmin(admin.ModelAdmin):
    list_display = ('id','name','pcourse','branch','cmpname','cmplogo','city','pyear','designation','stupic','pdate')
admin.site.register(placements,placementsAdmin)

class feeAdmin(admin.ModelAdmin):
    list_display = ('pcourse','branch1','branch2','branch3','hodname','seats','cfee','eligibility','due','cpic','pdate','sdate')
admin.site.register(fee,feeAdmin)

class facultyAdmin(admin.ModelAdmin):
    list_display = ('branch','tpic','des','name')
admin.site.register(faculty,facultyAdmin)
