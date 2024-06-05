from django import forms

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'departament': forms.Select(attrs={'class': 'form-control'}),

        }

    def clean(self):
        cleaned_data = super().clean()


        get_email = cleaned_data.get('email')
        check_email = Trainer.objects.filter(email=get_email)
        if check_email:
            msg = 'This email is already registered.'
            self.add_error('email', msg)


        get_first_name = cleaned_data.get('first_name')
        get_last_name = cleaned_data.get('last_name')
        check_trainer = Trainer.objects.filter(first_name=get_first_name, last_name=get_last_name)
        if check_trainer:
            message = 'First name already registered.'
            self.add_error('first_name', message)
            message = 'Last name already registered.'
            self.add_error('last_name', message)


        return cleaned_data