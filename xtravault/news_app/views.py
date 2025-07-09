from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('All works!')


def categories(request, cat_id):
    return HttpResponse(f'{cat_id}')