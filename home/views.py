from django.shortcuts import render



from django.shortcuts import render
from django.views.generic import TemplateView




# TemplateView: este un view generic definit de Django folosita pentru a putea sa fie randata/afisata o pagina html;
class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'               #-calea catre pe care o dorim afisata;
