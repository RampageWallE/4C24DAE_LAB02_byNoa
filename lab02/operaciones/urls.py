from django.urls import path 

from . import views

app_name = 'operaciones'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar_op', views.enviar_op, name='enviar_op'),
]