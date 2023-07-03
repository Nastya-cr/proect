from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('домашка по 4 лекции')