from django.urls import path 

from . import views

app_name = 'volumencilindro'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar_vol', views.enviar_vol, name='enviar_vol'),
]