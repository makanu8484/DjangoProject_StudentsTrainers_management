from django.urls import path

from intro import views

urlpatterns = [
    path('index/', views.hello, name='index'),
    path('show/', views.show_my_name, name='show_name'),
    path('list_cars/', views.cars, name='list_cars'),
    path('list_movies/', views.movies, name='list_movies'),
]