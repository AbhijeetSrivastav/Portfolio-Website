from django.urls import path




from django.urls import path
from django.urls.resolvers import URLPattern

from . import views  # . means current directory i.e blog app

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About')
]