from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipe, name='listar_equipe'),
    path('Json/', views.listar_equipeJson, name='listar_equipeJson'),
    path('cadastrar/', views.cadastrar_pesquisador, name='cadastrar_pesquisador'),  # Nova rota para cadastrar pesquisador
]
