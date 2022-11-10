import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms  import UploadForm
from .models import Upload
import requests

# Create your views here.

def home(request):
    return render(request, 'index.html')

def aadharfront(request):
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = form.instance
            
            img = Upload.objects.last()
            header= {
                "Content-Type": "application/json",
            }
            r = requests.post('https://devbankstatement.digisparsh.in:8000/upload_Aadhar_card_front',files = {'file':image.file}, verify=False)
            d1 = eval(r.json())
            
            return render(request, 'main.html', {'form':form, 'image':image, 'r':d1})

    else:
        form = UploadForm()
       

    return render(request, 'main.html', {'form': form,})
                


