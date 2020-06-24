from django.urls import path

from .views import index   #<----- direcionamento para as views teste


urlpatterns = [
    path('', index, name='index'),
]

