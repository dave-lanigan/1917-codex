from rest_framework import routers
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


# router = routers.DefaultRouter()
# router.register('api/content', ContentViewSet, 'content')
# urlpatterns = router.urls
app_name = 'api'
urlpatterns = [
    path('api/v0/codex/', views.all),
    path('api/v0/codex/<str:book_num>/', views.content_book),
    path('api/v0/canons/', views.canons),
    #path('api/codex/<int:book_num>', views.book),
    #path('api/codex/<str:book>', views.book),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
