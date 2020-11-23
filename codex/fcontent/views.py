from django.shortcuts import render
import requests
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


# https://docs.microsoft.com/en-us/dotnet/standard/net-standard


def index(request):
    return render(request, "fcontent/index1.html")


"""
h1 = Books
h2 = Parts
h3 = sections
h4 = titles
h5 = chapters
h6 = articles
-- = canons

"""
