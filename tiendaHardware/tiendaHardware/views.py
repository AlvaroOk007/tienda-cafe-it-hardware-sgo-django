from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request,'inicio.html',{})