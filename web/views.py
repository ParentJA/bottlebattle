__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.shortcuts import render


def home_view(request):
    return render(request, 'web/home.html')