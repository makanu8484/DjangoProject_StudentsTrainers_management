from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from trainer.forms import TrainerForm
from trainer.models import Trainer


class TrainerCreateView(CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('home')


class TrainerListView(ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'
