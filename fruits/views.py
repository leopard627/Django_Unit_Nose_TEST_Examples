from django.http import HttpResponse


def index(request):
    return HttpResponse("The index")


def show(request, fruit):
    return HttpResponse("Show the %s page" % fruit)


def add(request):
    return HttpResponse("Add a fruit")
