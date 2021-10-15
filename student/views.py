from .forms import StudentForm

def student_page(request):
    	form = StudentForm()
    	context = {
        	'form': form
    	}
    return render(request,'student/student.html', context)