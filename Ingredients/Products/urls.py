from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
#URL config
urlpatterns = [
  path('image', views.display_img)
]