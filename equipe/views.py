from django.shortcuts import render
from .models import Pesquisador
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse 

def listar_equipe(resquest):
    pesquisadores = Pesquisador.objects.all()
    return render(resquest, 'equipe.html', {'pesquisadores': pesquisadores})

def listar_equipeJson(resquest):
    pesquisadores = Pesquisador.objects.all()
    pesquisadores_data = list(pesquisadores.values())
    return JsonResponse(pesquisadores_data, safe=False)

# Serve para esativar proteção CSRF para uma view específica no Django.
@csrf_exempt
def cadastrar_pesquisador(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nome = data.get('nome')
        nivel = data.get('nivel')
        lattes = data.get('lattes')
        linkedin = data.get('linkedin')
        researchgate = data.get('researchgate')
        email = data.get('email')
        cargo = data.get('cargo')

        pesquisador = Pesquisador.objects.create(
            nome=nome,
            nivel=nivel,
            lattes=lattes,
            linkedin=linkedin,
            researchgate=researchgate,
            email=email,
            cargo=cargo
        )

        return JsonResponse({'mensagem': 'Pesquisador cadastrado com sucesso!'})

    else:
        return JsonResponse({'erro': 'Apenas requisições POST são permitidas.'}, status=405)