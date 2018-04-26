from django.shortcuts import render
from django.http import HttpResponse
from appCache.models import Page
from urllib.request import urlopen, URLError

# Create your views here.

def http(url):
    if (url.startswith("http://")) or (url.startswith("https://")):
        return url
    else:
        url = ("http://") + url
    return url

def process (request, resource):
    try: # está guardada
        pagina = Page.objects.get(url=resource)
        respuesta = pagina.content
    except Page.DoesNotExist:
        respuesta = "Url no guardada en diccionario"
        url = http(resource)
        try: 
            with urlopen(url) as nf:
                cont = nf.read()
                pagina = Page(url = resource, content = cont)
                respuesta += "<br/>Guardando..."
                pagina.save() #introduzco a mi dicc.
                respuesta += " guardada correctamente.<br/>Refresque para ir al sitio."
        except URLError:
            respuesta = "Url incorrecta"
    return HttpResponse (respuesta)

def error (request,resource):
    respuesta = "Para un uso correcto, introduzca: <b>localhost:8000/{url}</b>"
    return HttpResponse (respuesta)
