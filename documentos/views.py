from django.shortcuts import render
from .models import Documentos
from django.http import FileResponse, HttpResponseNotFound
import os

def view_pdf(request, filename):
    pdf_path = os.path.join('pdfs', filename)
    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponseNotFound('PDF not found')