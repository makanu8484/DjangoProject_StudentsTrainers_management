from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models

class Trainer(LoginRequiredMixin, models.Model):
    option_departament = [
        ('B', 'Backend'),
        ('F', 'Frontend'),
        ('N', 'Network')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    departament = models.CharField(choices=option_departament, max_length=40)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
