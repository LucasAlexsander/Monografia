from django.shortcuts import render, redirect, get_object_or_404
from .models import Pesquisador
from .forms import PesquisadorForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse 

def listar_equipe(resquest):
    pesquisadores = Pesquisador.objects.all()
    return render(resquest, 'equipe.html', {'Pesquisadores': pesquisadores})

def adicionar_pesquisador(request):
    form = PesquisadorForm()
    if request.method == 'POST':
        form = PesquisadorForm(request.POST)
        if form.is_valid(): 
            post = form.save()
            post.save()
            pesquisador = Pesquisador.objects.all()
            return redirect('/equipe', {'Pesquisadores': pesquisador})
        
    return render(request, 'adicionar_pesquisador.html', {'form': form})
            
def deletar_pesquisador(request, pesquisador_id):
    pesquisador = get_object_or_404(Pesquisador, id=pesquisador_id)
    pesquisador.delete()

    pesquisadores = Pesquisador.objects.all()
    return redirect('/equipe', {'Pesquisadores': pesquisadores})

def listar_equipeJson(resquest):
    pesquisadores = Pesquisador.objects.all()
    pesquisadores_data = list(pesquisadores.values())
    return JsonResponse(pesquisadores_data, safe=False)

def editar_pesquisador(request, pesquisador_id=None):  # Aceita o parâmetro pesquisador_id
    # Se o pesquisador_id for fornecido, recuperar o documento correspondente
    pesquisador = None
    if pesquisador_id is not None:
        pesquisador = Pesquisador.objects.get(pk=pesquisador_id)

    if request.method == 'POST':
        form = PesquisadorForm(request.POST, instance=pesquisador)  # Passa a instância do pesquisador para o formulário
        if form.is_valid(): 
            form.save()
            
            pesquisadores = Pesquisador.objects.all()
            return redirect('/equipe', {'Pesquisadores': pesquisadores})
    else:
        form = PesquisadorForm(instance=pesquisador)  # Passa a instância do pesquisador para o formulário

    pesquisadores = Pesquisador.objects.all()
    return render(request, 'adicionar_pesquisador.html', {'form': form, 'Pesquisadores': pesquisadores})

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