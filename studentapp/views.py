from django.shortcuts import redirect,render
from studentapp.models import StudentDetails

def addStudent(request):
    return render(request,'addstudent.html')

def add_student_details(request):
    if request.method=='POST':
        sname = request.POST['student_name']
        splace = request.POST['place']
        sage = request.POST['age']
        smarks = request.POST['marks']
        simage = request.FILES.get('file')
        
        student=StudentDetails(student_name=sname,
                               place=splace,
                               age=sage,
                               marks=smarks,
                               user_image=simage)
        student.save()
        print("added")
        return redirect('show_students')
    
def show_students(request):
    students=StudentDetails.objects.all()
    return render(request,'showPing.html',{'student':students})

def editpage(request,bell):
    students=StudentDetails.objects.get(id=bell)                            #.....select * from tablename where id = 56;
    return render(request,'edit.html',{'students':students})

def edit_student_details(request,bell):
    if request.method=='POST':
        students = StudentDetails.objects.get(id=bell)
        students.student_name = request.POST.get('student_name')
        students.place = request.POST.get('place')
        students.age= request.POST.get('age')
        students.marks = request.POST.get('marks')
        students.user_image = request.FILES.get('file')
        students.save()
        return redirect('show_students')
    return render(request,'edit.html')

# def deletepage(request,bell):
#     students=StudentDetails.objects.get(id=bell)
#     return render(request,'delete.html',{'students':students})

#Deleting student Element..
def delete_student(request,bell):
    students=StudentDetails.objects.get(id=bell)
    students.delete()
    return redirect('show_students')