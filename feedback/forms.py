from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from feedback.models import Feedback


class FeedbackForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 3}),
            'create_at': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Create Date', 'type': 'date'}),
            'update_at': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Update Date', 'type': 'date'}),
            'trainer': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Trainer'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()


        get_first_name = cleaned_data.get('first_name')
        get_last_name = cleaned_data.get('last_name')
        check_name = Feedback.objects.filter(first_name=get_first_name, last_name=get_last_name)
        if check_name:
            message = 'First name already in use.'
            self.add_error('first_name', message)
            message = 'Last name already in use.'
            self.add_error('last_name', message)


        get_email = cleaned_data.get('email')
        check_email = Feedback.objects.filter(email=get_email)
        if check_email:
            message = 'Email already in use.'
            self.add_error('email', message)


        check_message = cleaned_data.get('message')
        if len(check_message) < 10:
            msg = 'Description must be at least 10 characters.'
            self.add_error('message', msg)


        return cleaned_data