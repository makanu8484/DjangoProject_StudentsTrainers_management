from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render




@login_required()
def hello(request):
    return HttpResponse("Hello World!")

@login_required()
def show_my_name(request):
    return HttpResponse("Hello, Iulian!")
@login_required()
def cars(request):
    context = {
        'all_cars':
        [
            {
                'name': 'Volvo',
                'model': 'XC90',
                'color': 'blue',
                'year': 2020,
            },
            {
                'name': 'BMW',
                'model': 'M3',
                'color': 'red',
                'year': 2022,
            },
            {
                'name': 'Tesla',
                'model': 'Model X',
                'color': 'green',
                'year': 2021,
            }
        ]
    }
    return render(request, template_name='intro/list_of_cars.html', context=context)
@login_required()
def movies(request):
    context = {
        'all_movies':
            [
                {
                    'name': 'Home Alone',
                    'type': 'Comedy',
                    'year': 1995,
                    'director': 'Cris Columbus',
                },
                {
                    'name': 'Matrix',
                    'type': 'Action',
                    'year': 1998,
                    'director': 'Lana Wachovia',
                },
                {
                    'name': 'Saw',
                    'type': 'Horror',
                    'year': 2017,
                    'director': 'James Wan',
                }
            ]
    }
    return render(request, template_name='intro/list_of_movies.html', context=context)
