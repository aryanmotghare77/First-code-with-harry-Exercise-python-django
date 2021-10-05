from django.http import HttpResponse
def button(request):
    return HttpResponse("<a href=https://www.djangoproject.com/><button>Got o django documentation</button></a>")
