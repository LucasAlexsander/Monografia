from django.urls import path
from . import views

urlpatterns = [
    path('pdfs/<str:filename>/', views.view_pdf, name='view_pdf'),
    path('', views.listar_documentos, name='listar_documentos'),
    path('adicionar/', views.adicionar, name='adicionar_documento'),
    path('editar/<int:documento_id>/', views.editar, name='editar'),
    path('deletar/<int:documento_id>/', views.deletar, name='deletar'),
]