from pathlib import Path
from django.shortcuts import render
import requests
from django import template
from django.template.defaultfilters import stringfilter
import pymongo
import json


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

with open(str(BASE_DIR.parent.parent)+"/codex-config.json") as f:
    conf = json.load(f)


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
