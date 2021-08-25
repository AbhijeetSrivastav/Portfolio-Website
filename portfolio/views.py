# Create your views here.

from django.http.response import HttpResponse
from django.template import context, loader
from django.shortcuts import render

def home(request):
    context = {'test':'test'}
    return render(request, 'portfolio/main.html', context)


def about(request):
    context = {'test':'test'}
    return render(request, 'portfolio/main.html', context)



# ------------------------------------------------
"Another way to show html"
"""template = loader.get_template('portfolio/main.html')
    context = {}
    return HttpResponse(template.render(context, request))"""