# infos/urls.py
from django.urls import path
from .views import mainpage, me, contact

urlpatterns = [
   path('', mainpage),
   path('me', me),
   path('contact', contact),

]