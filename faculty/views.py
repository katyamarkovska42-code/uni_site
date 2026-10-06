from django.shortcuts import render, get_object_or_404
from .models import HomePage, Department, Program


def home(request):
    page = HomePage.objects.first()
    return render(request, "faculty/home.html", {"page": page})


def program_list(request):
    programs = Program.objects.select_related("department")
    return render(request, "faculty/program_list.html", {"programs": programs})


def program_detail(request, id):  # видаcть помилку, якщо не знайдено за id
    program = get_object_or_404(Program, id=id)
    subjects = program.subjects.splitlines()
    return render(
        request,
        "faculty/program_detail.html",
        {"program": program, "subjects": subjects},
    )


def department_list(request):
    departments = Department.objects.all()
    return render(request, "faculty/department_list.html", {"departments": departments})


def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    return render(request, "faculty/department_detail.html", {"department": department})
