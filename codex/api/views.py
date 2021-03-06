from pathlib import Path
from django.shortcuts import render
from django.http import JsonResponse
import regex
import pymongo
import json


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

with open(str(BASE_DIR.parent.parent)+"/codex-config.json") as f:
    conf = json.load(f)


def parse_bson(curser):
    out = list(curser)
    l = []
    for i, mass in enumerate(out):
        mass["_id"] = str(mass["_id"])
        l.append(mass)
    return l


def get_num(tag):
    return tag[:tag.find("-")], int(tag[tag.find("-")+1:])


def all(request, format=None):
    client = pymongo.MongoClient(conf["db"])
    db = client["codex"]
    coll = db["api_content"]
    return JsonResponse(list(parse_bson(coll.find()))[0]["book"], safe=False)


def canons(request, format=None):
    client = pymongo.MongoClient(conf["db"])
    db = client["codex"]
    coll = db["canons"]
    out = coll.find()

    return JsonResponse(parse_bson(coll.find()), safe=False)


def content_book(request, book_num):
    client = pymongo.MongoClient(conf["db"])
    db = client["codex"]
    coll = db["api_content"]

    books = ["book-1_general-principles-of-canon-law",
             "book-2_laws-concerning-persons",
             "book-3_sacred-things",
             "book-4_canonical-trials",
             "book-5_offences-and-penalties"]

    for book in books:
        if book.find(book_num) != -1:

            resp = JsonResponse(list(coll.find())[0]["book"][book], safe=False)
            #resp['Access-Control-Allow-Origin'] = "localhost:8000"
            resp['Access-Control-Allow-Origin'] = "http://iudicabit.mywire.org"
            #resp['Access-Control-Allow-Origin'] = "*"
            return resp
