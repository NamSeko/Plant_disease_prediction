from django.shortcuts import render # type: ignore
from .ml import get_classify
from django.conf import settings
import os

# Create your views here.
def index(request):
    context = {
        'status':'Tải ảnh của bạn ở đây.'
    }
    return render(request, 'seminar/index.html', context)

def result(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
            
        if image_file:
            classer = get_classify(image_file)
            context = {
                'status': classer,
            }
        else:
            context = {
                'status': 'Bạn vui lòng tải lại ảnh !!!'
            }
        return render(request, 'seminar/index.html', context)


