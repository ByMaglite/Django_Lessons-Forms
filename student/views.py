from django.shortcuts import render
from student.forms import StudentForm

def index(request):
    return render(request, 'student/index.html')


def student_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')  
    context = {
        'form': form
    }
    return render(request,'student/student.html', context)
