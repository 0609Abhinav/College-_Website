from django.urls import path
from. import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('courses/',views.courses),
    path('placements/',views.placement),
    path('signup/',views.signup),
    path('gallery/',views.imagegallery),
    path('recruiters/',views.recruitersd),
    path('fees/',views.fees),
    path('faculty/',views.facultys),


 ]