from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'news_app/index.html')


def categories(request):
    return HttpResponse()


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Not found aaaaa</h1>")