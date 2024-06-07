from django.urls import path

from student import views


urlpatterns = [

    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
    path('list_students/', views.StudentListView.as_view(), name='list_students'),
    path('update_student/<int:pk>', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete_student/<int:pk>', views.StudentDeleteView.as_view(), name='delete_student'),
    path('details_student/<int:pk>', views.StudentDetailView.as_view(), name='details_student'),
]