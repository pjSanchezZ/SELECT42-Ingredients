from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls import include, url
from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#URL config

urlpatterns = [
    url(r'^cart/', views.cart), 
    url(r'^change_password/', views.change_password), 
    url(r'^checkout/', views.checkout), 
    url(r'^deactivate_account/', views.deactivate_account), 
    url(r'^faq/', views.faq), 
    url(r'^fresh_vegan/', views.fresh_vegan), 
    url(r'^help_support/', views.help_support), 
    url(r'^listing/', views.listing), 
    url(r'^my_account/', views.my_account), 
    url(r'^my_address/', views.my_address), 
    url(r'^my_order/', views.my_order), 
    url(r'^picks_today/', views.picks_today), 
    url(r'^privacy/', views.privacy), 
    url(r'^product_details/', views.product_details), 
    url(r'^promo_details/', views.promo_details), 
    url(r'^promos/', views.promos), 
    url(r'^recommend/', views.recommend), 
    url(r'^refund_payment/', views.refund_payment), 
    url(r'^review/', views.review), 
    url(r'^search/', views.search), 
    url(r'^signin/', views.signin), 
    url(r'^signup/', views.signup), 
    url(r'^status_canceled/', views.status_canceled), 
    url(r'^status_complete/', views.status_complete), 
    url(r'^status_onprocess/', views.status_onprocess), 
    url(r'^successful/', views.successful), 
    url(r'^terms_conditions/', views.terms_conditions), 
    url(r'^terms&conditions/', views.terms_and_conditions), 
    url(r'^verification/', views.verification), 
    url(r'^home/', views.home),
    url(r'^find/', views.search_test),
    url(r'^range/', views.ranger),
    url(r'^details/', views.details),
<<<<<<< HEAD
    url(r'^list/', views.listing_search),
    url(r'^try/', views.try_search),
=======
    url(r'^list/', views.list_test),
    url(r'^login/', views.login),
    url(r'^signup1/', views.signup1),
>>>>>>> main
]