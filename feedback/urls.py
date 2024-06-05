from django.urls import path

from feedback import views

urlpatterns = [

    path('create_feedback/', views.FeedbackCreateView.as_view(), name='create_feedback'),
    path('feedback_list/', views.FeedbackListView.as_view(), name='feedback_list'),
]