from django.http import HttpResponse
def pagina1(request): 
    return HttpResponse("Hola")

def pagina2(request): 
    return HttpResponse("Hola 2")

def pagina3(request): 
    return HttpResponse("Hola 3")
