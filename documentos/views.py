from django.shortcuts import render
from .models import Documentos
from django.http import FileResponse, HttpResponseNotFound
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