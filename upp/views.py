# upp/views.py
from django.shortcuts import render
from .utils import capture_and_ocr

def capture_and_ocr_view(request):
    text = capture_and_ocr()
    return render(request, 'upp/ocr_result.html', {'text': text})
