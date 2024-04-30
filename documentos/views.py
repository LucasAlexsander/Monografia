from django.shortcuts import render, redirect, get_object_or_404
from .models import Documentos
from . forms import DocumentosForm
from django.http import FileResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from documentos.functions import handle_uploaded_file
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

def view_pdf(request, filename):
    pdf_path = os.path.join('documentos/pdfs', filename)
    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponseNotFound('PDF not found')

def listar_documentos(request):
    ordenacao = request.GET.get('ordenacao', 'default')  # Obter parâmetro de ordenação da query string
    documentos = Documentos.objects.all()
    ordenacao_direcao = ''

    if ordenacao == 'titulo':
        documentos = documentos.order_by('titulo')
    elif ordenacao == '-titulo':
        documentos = documentos.order_by('-titulo')
    elif ordenacao == 'data':
        documentos = documentos.order_by('dataEntrega')
    elif ordenacao == '-data':
        documentos = documentos.order_by('-dataEntrega')

    # Paginação
    paginator = Paginator(documentos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_numbers = [n for n in range(page_obj.number - 2, page_obj.number + 3) if 0 < n <= page_obj.paginator.num_pages] 
    
    # Adicione o parâmetro de ordenação à URL dos links de paginação
    print("Query string:", request.META['QUERY_STRING'])

    if ordenacao:
        ordenacao_param = f"&ordenacao={ordenacao}"
        page_obj.url_suffix = ordenacao_param if '?' in request.META['QUERY_STRING'] else f"?ordenacao={ordenacao}"


    # Verificar se o número da página é menor que 1 e, se for, definir como 1
    if page_obj.number < 1:
        page_obj.number = 1
        
    return render(request, 'documentos.html', {'Documentos': page_obj, 'page_numbers': page_numbers, 'ordenacao': ordenacao})

def adicionar(request):
    form = DocumentosForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = DocumentosForm(request.POST, request.FILES)
        if form.is_valid(): 
            handle_uploaded_file(request.FILES['arquivo'])
            model_instace = form.save(commit=False)
            model_instace.save()
            model_instace.autor.set(form.cleaned_data['autor'])
            model_instace.orientador.set(form.cleaned_data['orientador'])
            model_instace.coorientador.set(form.cleaned_data['coorientador'])
            
            documentos = Documentos.objects.all()
            return redirect('/documentos', {'Documentos': documentos})
    else:
        form = DocumentosForm()
        return render(request, 'adicionar_documento.html', {'form': form})
        
    return render(request, 'adicionar_documento.html', {'form': form})

def editar(request, documento_id=None):  # Aceita o parâmetro documento_id
    # Se o documento_id for fornecido, recuperar o documento correspondente
    documento = None
    if documento_id is not None:
        documento = Documentos.objects.get(pk=documento_id)

    if request.method == 'POST':
        form = DocumentosForm(request.POST, request.FILES, instance=documento)  # Passa a instância do documento para o formulário
        if form.is_valid(): 
            form.save()
            
            documentos = Documentos.objects.all()
            return redirect('/documentos', {'Documentos': documentos})
    else:
        form = DocumentosForm(instance=documento)  # Passa a instância do documento para o formulário

    documentos = Documentos.objects.all()
    return render(request, 'adicionar_documento.html', {'form': form, 'documentos': documentos})

def deletar(request, documento_id):
    documento = get_object_or_404(Documentos, id=documento_id)
    documento.delete()

    documentos = Documentos.objects.all()
    return redirect('/documentos', {'Documentos': documentos})
