from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Student
from myapp.forms import StudentForm
# Create your views here.


def display(request):
    sort_by = request.GET.get('sort', 'name')
    query = request.GET.get('q', '').strip()

    allowed_sorting = {
        'name': 'name',
        'name_desc': '-name',
        'age_asc': 'age',
        'age_desc': '-age',
        'dob_newest': '-dob',
        'dob_oldest': 'dob',
    }

    ordering = allowed_sorting.get(sort_by, 'name')

    students = Student.objects.all()

    # Search across all student records
    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(place__icontains=query)
        )

    # Sort the filtered records
    students = students.order_by(ordering, 'id')

    # Paginate the results
    paginator = Paginator(students, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    
    context = {
    'stud': page_obj,
    'page_obj': page_obj,
    'total_students': Student.objects.count(),
    'matching_students': paginator.count,
    'current_sort': sort_by,
    'search_query': query,
}

    return render(request, 'myapp/index.html', context)


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