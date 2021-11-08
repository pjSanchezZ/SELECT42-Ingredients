from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
#URL config
urlpatterns = [
  path('search_results', views.search_test, name='search_result'),
]