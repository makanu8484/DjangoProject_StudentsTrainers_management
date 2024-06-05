from django.shortcuts import render



from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackCreateView(CreateView):
    template_name = 'feedback/create_feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('home')#


class FeedbackListView(ListView):
    template_name = 'feedback/feedback_list.html'
    model = Feedback
    context_object_name = 'all_feedback'



    def get_queryset(self):
        return Feedback.objects.all()