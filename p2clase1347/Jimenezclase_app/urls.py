from django.urls import path
from . import views
urlpatterns = [
    path('',views.hola, name='hola'),
    path('mimama/',views.Mi_mama, name='mimama'),
    
]