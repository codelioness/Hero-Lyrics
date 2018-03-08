from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Holding page: Index")

def song(request):
    return HttpResponse("Holding page: Song")