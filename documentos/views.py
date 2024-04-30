from django.shortcuts import render, redirect, get_object_or_404
from .models import Documentos
from . forms import DocumentosForm
from django.http import FileResponse, HttpResponseNotFound, JsonResponse
from documentos.functions import handle_uploaded_file
import os

def view_pdf(request, filename):
    pdf_path = os.path.join('documentos/pdfs', filename)
    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponseNotFound('PDF not found')

def listar_documentos(resquest):
    documentos = Documentos.objects.all()
    return render(resquest, 'documentos.html', {'Documentos': documentos})

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
