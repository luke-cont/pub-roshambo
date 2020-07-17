from django.shortcuts import render, redirect
from random import choice


CHOICE = ['r', 'p', 's']


def index(request):
    return render(request, 'personal/home.html')
