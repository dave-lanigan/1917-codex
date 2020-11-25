from django.shortcuts import render
import requests
from django import template
from django.template.defaultfilters import stringfilter
import pymongo
import json


CONF_PATH = "/home/david/Dev/judica-me-additional/1917-codex/config.json"
with open(CONF_PATH, "r") as f:
    conf = json.load(f)

# https://docs.microsoft.com/en-us/dotnet/standard/net-standard


def index(request):
    return render(request, "fcontent/index1.html")


def index2(request):
    return render(request, "fcontent/index2.html")


def canon_search(request):
    out = request.GET['search']
    client = pymongo.MongoClient(conf["db"])
    db = client["codex"]
    coll = db["canons"]
    search_list = coll.find(
        {"$text": {"$search": out}})

    return render(request, "fcontent/canon_search.html", {"data": search_list})


"""
h1 = Books
h2 = Parts
h3 = sections
h4 = titles
h5 = chapters
h6 = articles
-- = canons

"""
