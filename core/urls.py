from django.urls import path

from .views import index   #<----- direcionamento para as views


urlpatterns = [
    path('', index, name='index'),
]
