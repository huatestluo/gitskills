from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world! django __')

def huahua(request):
    return HttpResponse('huahua, django __')