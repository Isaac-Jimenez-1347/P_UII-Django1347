from django.urls import path
from . import views
urlpatterns = [
    path('',views.hola, name='Jimenezclase_app'),
    path('minovia',views.minovia, name='minovia'),
]