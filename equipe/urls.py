from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipe, name='listar_equipe'),
    path('Json/', views.listar_equipeJson, name='listar_equipeJson'),
    path('cadastrar/', views.cadastrar_pesquisador, name='cadastrar_pesquisador'),  # Nova rota para cadastrar pesquisador
    path('adicionar/', views.adicionar_pesquisador, name='adicionar_pesquisador'),
    path('deletar/<int:pesquisador_id>/', views.deletar_pesquisador, name='deletar_pesquisador'),
    path('editar/<int:pesquisador_id>/', views.editar_pesquisador, name='editar_pesquisador'),
]
