from django.urls import path

from trainer import views

urlpatterns = [
    path('create_trainer', views.TrainerCreateView.as_view(), name='create_trainer'),
    path('list_trainers', views.TrainerListView.as_view(), name='list_trainers'),

]