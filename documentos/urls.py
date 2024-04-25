from django.urls import path
from . import views

urlpatterns = [
    path('<str:filename>/', views.view_pdf, name='view_pdf'),
    path('', views.listar_documentos, name='listar_documentos'),
]