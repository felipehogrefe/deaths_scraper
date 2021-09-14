from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'investimentos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('importar/', views.importar_preferencias, name='importar'),
    path('exportar/', views.exportar_preferencias, name='exportar'),
    path('buscar_acao/', views.buscar_acao, name='buscar_acao')
]