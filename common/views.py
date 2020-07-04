from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='common/index.html')
