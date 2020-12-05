from . import views
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('api/v0/codex/', views.all),
    path('api/v0/codex/<str:book_num>/', views.content_book),
    path('api/v0/canons/', views.canons),
]
