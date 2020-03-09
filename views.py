from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
def index(request):
	return render(request,"calcapp/index.html")
def calclogic(request):
    a= request.POST["txtnum1"] #to fetch data from textfield
    b = request.POST["txtnum2"]
    if request.POST["btnsubmit"]=="+":
     c=int(a)+int(b)
    elif request.POST["btnsubmit"]=="-":
     c=int(a)-int(b) 
    elif request.POST["btnsubmit"]=="*":
     c=int(a)*int(b)
    else:
     c= int(a)/int(b) 
    return render(request,"calcapp/index.html",{'key':"result is "+str(c),'key1':a,'key2':b})	
def courseinfo(request):
   if request.method=="POST":
      basic = request.POST.getlist('c[]')
      advance = request.POST['adcourse']
      country = request.POST['country']
      state = request.POST.getlist('state[]')
      s=''
      for s1 in basic:
        s=s+s1+" "
      s2=''
      for s3 in state:
        s2= s2+s3 +" " 
      name = request.POST["txtname"]  
      date = request.POST["txtdate"]
      fees = request.POST["txtfees"]
      query = request.POST["query"]
      result = {'basic':"basic course is "+s,'advance':" Advance course is "+advance,'country':"Selected Country is "+country,'state':" State is "+s2,'name':'name is '+name,'date ':'date is '+date,'fees':'fees is '+str(fees),'query':'query is '+query}
      return render(request,"calcapp/course.html",{'msg':result.values()}) 
   return render(request,"calcapp/course.html")  

def studentinfo(request):
    if request.method == "POST":
       res = Student.objects.get(rno=int(request.POST["txtrno"]))
       if res:
        return render(request,"calcapp/studentinfo.html",{"msg":"Rno Already exist"})  
       else:
        s = Student(rno=int(request.POST["txtrno"]),sname=request.POST["txtname"],branch=request.POST["txtbranch"],fees = int(request.POST["txtfees"]))
        s.save()
        return redirect("viewstudent")
        
    return render(request,"calcapp/studentinfo.html")

def viewstudent(request):
    s = Student.objects.all()  # select * from student

    return render(request,"calcapp/viewstudent.html",{'res':s})
def findstudent(request):
    if request.method == "POST":
      s1 = Student.objects.get(pk=request.POST["txthid"]) 
      s1.rno=int(request.POST["txtrno"])
      s1.sname=request.POST["txtname"]
      s1.branch=request.POST["txtbranch"]
      s1.fees=int(request.POST["txtfees"])
      s1.save()
      return redirect("viewstudent")
    else:  
     s = Student.objects.get(pk=request.GET["q"])
     return render(request,"calcapp/findstudent.html",{"res":s})  
def deletestudent(request):
    if request.method == "POST":
      s1 = Student.objects.get(pk=request.POST["txtid"])
      s1.delete()
      return redirect("viewstudent")
    else:  
     s = Student.objects.get(pk=request.GET["q"])
     return render(request,"calcapp/deletestudent.html",{"res":s})    



