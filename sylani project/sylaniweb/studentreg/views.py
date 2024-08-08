from django.shortcuts import render
from django.http import HttpResponseRedirect
from studentreg.models import students,campus
from django.contrib import messages


# Create your views here.
def register(request):
    
    
    if request.method=='POST':
     
        city=request.POST['city']
        course=request.POST['course']
        campuses=request.POST['campus']
        timing=request.POST['timing']
        name=request.POST['name']
        fname=request.POST['fname']
        email=request.POST['email']
        Phone=request.POST['phone']
        cnic=request.POST['cnic']
        fcnic=request.POST['fcnic']
        dob=request.POST['dob']
        address=request.POST['address']
        qulification=request.POST['qulification']
        laptop=request.POST['laptop']
        user1=students.objects.filter(cnic=cnic).first()
        
        
        if user1.course == course:
            messages.error(request,'you are arleady select this course')
            return render(request,'studentreg/register.html')

            
        elif user1.cnic==cnic:
            messages.warning(request,'yu are already enroll course')
            return render(request,'studentreg/register.html')
        elif user1.fcnic==fcnic:
            messages.warning(request,'yu are already enroll course')
            return render(request,'studentreg/register.html')
        else:
        
            student=students(city=city,course=course,campus=campuses,timing=timing,name=name,fname=fname,email=email,Phone=Phone,cnic=cnic,fcnic=fcnic,dob=dob,qulification=qulification,address=address,laptop=laptop)
            student.save()
            messages.info(request,f'{name} you are register successfully')
        

            return render(request,'studentreg/register.html')
    return render(request,'studentreg/register.html')
def data(request):
    if request.method=='POST':
        try:
            st=request.POST['Searching']
            if st in 'none':
                messages.warning(request,'please select catageries')
                return render(request,'studentreg/student.html')
            else:
                
                
                s=students.objects.filter(course=st)
                return render(request,'studentreg/student.html',{'stu':s})
        except:
            messages.warning(request,'please select catageries')
            return render(request,'studentreg/student.html')
            
    return render(request,'studentreg/student.html')
    
    
def result(request):
    a=['4230151026285','4230109653371']
    if request.method=="POST":
        search=request.POST['cnic']
        for i in a:
            if search==i:
                stu=students.objects.filter(cnic=search)
                return render(request,'studentreg/result.html',{'stu':stu})

    
    

    return render(request,'studentreg/result.html')