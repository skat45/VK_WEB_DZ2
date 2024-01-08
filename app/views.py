from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return render(request, 'index.html', context={'user': {'is_authorised': False}, 'items': range(10)})


def ask_page(request):
    return render(request, 'ask.html', context={'user': {'is_authorised': True, 'name': 'skat45'}})


def login_page(request):
    return render(request, 'login.html', context={'user': {'is_authorised': False}})


def register_page(request):
    return render(request, 'register.html', context={'user': {'is_authorised': False}})


def question_page(request, id):
    return render(request, 'question_page.html', context={'user': {'is_authorised': False, 'id': int(id)}})


def settings_page(request):
    return render(request, 'settings.html', context={'user': {'is_authorised': True, 'name': 'skat45',
                                                              'login': 'studik@student.bmstu.ru'}})
