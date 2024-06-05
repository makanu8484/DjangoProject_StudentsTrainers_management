from django.urls import path

from student import views






urlpatterns = [

    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
    path('list_students/', views.StudentListView.as_view(), name='list_students'),
]