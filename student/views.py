from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from student.forms import StudentForm
from student.models import Student


# CreateView -> este o clasa dezvoltata de Django care va ajuta sa va definiti un obiect
# in baza de date si afisarea unui formular asociat modelului definit in models.py (Student)
class StudentCreateView(CreateView):
    template_name = "student/create_student.html"
    model = Student                                # clasa din student/models.py;
    form_class = StudentForm                       # (formularul va avea toate fieldurile din model daca scriu '__all__');
    success_url = reverse_lazy('home')             # in momentul salvarii, utilizatorul va fi redirectionat catre pagina home;




# ListView -> este o clasa dezvoltata de Django care va ajuta pentru a afisa o lista de obiecte dintr-u model specificat;
class StudentListView(ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'

# Acesta metoda este responsabila pentru returtanarea unui Queryset care reprezinta obiectele din baza de date
# pe care doriti sa le afisati sau sa le manipulati in templates;
    def get_queryset(self):
        return Student.objects.filter(active=1)
        #return Student.objects.all()             # dorim sa afisam toata lista fara filter;
