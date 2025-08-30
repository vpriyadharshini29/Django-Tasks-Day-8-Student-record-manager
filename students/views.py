from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

# --- Function-Based View (FBV) ---
def home(request):
    return render(request, "students/home.html")

# --- Class-Based Views (CBVs) ---
class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"

class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_detail.html"

class StudentCreateView(CreateView):
    model = Student
    fields = ["name", "roll_no", "course", "age"]
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student-list")

class StudentUpdateView(UpdateView):
    model = Student
    fields = ["name", "roll_no", "course", "age"]
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student-list")

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("student-list")
class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"
    paginate_by = 5   # Show 5 students per page
