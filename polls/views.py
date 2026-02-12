from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the polls index.")

def create_poll(request):
    return HttpResponse("You're at the polls creator.")

def retrieve_poll(request):
    return HttpResponse("You're at the polls retrieve.")

def update_poll(request):
    return HttpResponse("You're at the polls update.")

def delete_poll(request):
    return HttpResponse("You're at the polls delete.")

