from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Student
from myapp.forms import StudentForm
# Create your views here.

def display(request):
    s=Student.objects.all()
    d={'stud':s}
    return render(request,'myapp/index.html',d)


def insert_view(request):
    if request.method == "POST":
        f = StudentForm(request.POST)

        if f.is_valid():
            f.save()
            return redirect('/')
    else:
        f = StudentForm()

    d = {'form': f}
    return render(request, 'myapp/insert.html', d)


def update_view(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'stud': student
    }

    return render(request, 'myapp/update.html', context)


def delete_view(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('/')

    return render(request, 'myapp/delete_confirm.html', {
        'student': student
    })