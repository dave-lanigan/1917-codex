from django.shortcuts import render
from django.http import JsonResponse
import regex
import pymongo
import json


CONF_PATH = "/home/david/Dev/judica-me-additional/1917-codex/config.json"
with open(CONF_PATH, "r") as f:
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
    pass
    client = pymongo.MongoClient(conf["db"])
    db = client["codex"]
    coll = db["api_content"]

    print(list(coll.find()))

    return JsonResponse(list(parse_bson(coll.find()))[0]["book"], safe=False)


def content_book(request, book_num):
    client = pymongo.MongoClient(conf["db"])
    db = client["codex"]
    coll = db["api_content"]

    books = ["book-1_general-principles-of-canon-law",
             "book-2_laws-concerning-persons"]

    for book in books:
        if book.find(book_num) != -1:
            return JsonResponse(list(coll.find())[0]["book"][book], safe=False)


def content_canons(request, book_num):
    pass


# def book(request, book_num):
#     codex = Content.objects.all()
#     codex = codex[0].__dict__["book"]
#     books_keys = list(codex.keys())
#     book = codex[books_keys[book_num-1]]

#     option = request.GET.get('option')

#     if option:
#         book = codex[books_keys[book_num-1]]
#         keys = list(book.keys())
#         if option == "canons-top":
#             d = {}
#             for key in keys:
#                 if key.find("canon-") != -1:
#                     d[key] = book[key]

#             return JsonResponse(d, safe=False)

#         if option == "canons-top-names":
#             l = []
#             for key in keys:
#                 if key.find("canon-") != -1:
#                     l.append(key.replace("-", " ").title())

#             return JsonResponse(l, safe=False)

#     if option is None:
#         return JsonResponse(book, safe=False)
#         # return JsonResponse(None, safe=False)
