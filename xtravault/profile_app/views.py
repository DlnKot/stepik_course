from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Main page")

def news(request):
    return HttpResponse("<h1>News<h1/>")