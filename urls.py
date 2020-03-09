from django.urls import path
from  . import views

urlpatterns = [

path('',views.index,name='index'),
path('calclogic',views.calclogic,name='calclogic'),
path('courseinfo',views.courseinfo,name='courseinfo'),
path('studentinfo',views.studentinfo,name='studentinfo'),
path('viewstudent',views.viewstudent,name='viewstudent'),
path('findstudent',views.findstudent,name='findstudent'),
path('deletestudent',views.deletestudent,name='deletestudent')

]