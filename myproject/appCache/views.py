from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def process (request, resource):
    respuesta = "Process"
    #proceso url, veo si está en dicc, introduzco al dicc (if), y muestro content
    return HttpResponse (respuesta)

def error (request,resource):
    respuesta = "Para un uso correcto, introduzca: <b>localhost:8000/{url}</b>"
    return HttpResponse (respuesta)
