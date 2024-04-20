from django.shortcuts import render
from .models import Pesquisador

# Create your views here.
# def listar_equipe(resquest):
#     return render(resquest, 'equipe.html')

def listar_equipe(resquest):
    pesquisadores = Pesquisador.objects.all()
    return render(resquest, 'equipe.html', {'pesquisadores': pesquisadores})