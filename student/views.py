from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from student.forms import StudentForm, StudentUpdateForm
from student.models import Student


# CreateView -> este o clasa dezvoltata de Django care va ajuta sa va definiti un obiect
# in baza de date si afisarea unui formular asociat modelului definit in models.py (Student)
class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = "student/create_student.html"
    model = Student                                # clasa din student/models.py;
    form_class = StudentForm                       # (formularul va avea toate fieldurile din model daca scriu '__all__');
    success_url = reverse_lazy('home')             # in momentul salvarii, utilizatorul va fi redirectionat catre pagina home;




# ListView -> este o clasa dezvoltata de Django care va ajuta pentru a afisa o lista de obiecte dintr-u model specificat;
class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'

# Acesta metoda este responsabila pentru returtanarea unui Queryset care reprezinta obiectele din baza de date
# pe care doriti sa le afisati sau sa le manipulati in templates;

    def get_queryset(self):
        return Student.objects.filter(active=1)
        #return Student.objects.all()             # dorim sa afisam toata lista fara filter;


# Este o clasa dezvoltata de django care simplifica procesul de actualizare a datelor dintr o baza de date pe baza unui formular;
class StudentUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list_students')

# DeleteView -> este o clasa dezvoltata de Django care este utilizata pentru stergerea unui obiect( a unei inregistrari);
class StudentDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_students')

# DetailView -> este o clasa dezvoltate de Django care este utilizata pentru afisarea informatiilor despre obiectul
# respectiv(inregistrarea stocata in db);
class StudentDetailView(LoginRequiredMixin,DetailView):
    template_name = 'student/details_students.html'
    model = Student

