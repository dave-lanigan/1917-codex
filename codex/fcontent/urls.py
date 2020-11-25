from django.urls import path
from django.conf.urls import url
from . import views

app_name = "fcontent"
urlpatterns = [
    path('', views.index, name='index'),
    path('book-1', views.index, name='index'),
    path('book-2', views.index2, name='book2'),
    path('canon-search', views.canon_search, name='canon_search')
]
