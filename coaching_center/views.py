from django.shortcuts import render

# Create your views here.

    
    
def home(request):
    return render(request,'input.html')
    
    
def findstaff(request):
    staff_name1='Riya'
    staff_name2='John'
    staff_name3='Alex'
    
    course_name= request.GET['course']
    if course_name=='Python':
        staff= staff_name1
    elif course_name=='Java':
        staff=staff_name2
    elif course_name=='R':
        staff= staff_name3
    else:
        return 'None'
    
    return render(request,'output.html',{'staff1':staff})
    
    
