from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from student.models import Student


class StudentForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'           # formularul va avea toate fieldurile din model daca scriu '__all__';



        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriptions', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start date', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'End date', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),

        }

# Metoda clean este folosita pentru a verifica corectitudinea datelor introduse.
# Atunci cand facem un formular trebuie sa implementam validari personalizate care sa se aplice
# pe intregul formular.

    def clean(self):
        cleaned_data = super().clean()

# O validare in care adresa de email sa fie unica. Daca ea este deja salvata sa genereze eroare in formular;
        # Varianta 1:
        #     get_email = cleaned_data.get('email')
        #     all_students = Student.objects.all()
        #     for student in all_students:
        #         if student.email == get_email:
        #             print('EXISTA DEJA')

        # Varianta 2:
        get_email = cleaned_data.get('email')
        check_email = Student.objects.filter(email=get_email)
        if check_email:
            msg = 'Email already registered'
            self.add_error('email', msg)

# O validare pentru first_name si last_name. Nu putem salva un student (first_name si last_name) daca exista unul asemanator in db;


        get_first_name = cleaned_data.get('first_name')
        get_last_name = cleaned_data.get('last_name')
        check_student = Student.objects.filter(first_name=get_first_name, last_name=get_last_name)
        if check_student:
            message_first_name = 'First Name already registered'
            self.add_error('first_name', message_first_name)

            message_last_name = 'Last Name already registered'
            self.add_error('last_name', message_last_name)

# O validate pe start_date si end_date. Daca start_date este mai mare decat end_date sa afisam o eroare;

        get_start_date = cleaned_data.get('start_date')
        get_end_date = cleaned_data.get('end_date')
        if get_start_date > get_end_date:
            msg = 'Start date must be before end date'
            self.add_error('start_date', msg)
            msg = 'End date must be after start date'
            self.add_error('end_date', msg)


# O validare in care utilizatorul este obligat sa introduca minim 10 caractere in campul description;

        get_description = cleaned_data.get('description')
        if len(get_description) < 10:
            msg = 'Description must be at least 10 characters'
            self.add_error('description', msg)

        return cleaned_data


class StudentUpdateForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'           # formularul va avea toate fieldurile din model daca scriu '__all__';



        widgets = {
            
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriptions', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start date', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'End date', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),

        }