import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms  import FUploadForm, BUploadForm,BankForm, PUploadForm
from .models import BUpload, FUpload, BankStatement, PUpload
import requests
from django.template.defaulttags import register


def home(request):
    return render(request, 'index.html')


############################ AADHAR CARD ######################################

def aadhar(request):
    if request.method == 'POST':
        formf = FUploadForm(request.POST, request.FILES or None)
        formb = BUploadForm(request.POST, request.FILES or None)

        if all([formf.is_valid(), formb.is_valid()]):
            formf.save()
            image1 = formf.instance
            formb.save()
            imageab = formb.instance
            r1 = requests.post('https://devbankstatement.digisparsh.in:8000/upload_Aadhar_card_front',files = {'file':image1.filef}, verify=False)
            r2 = requests.post('https://devbankstatement.digisparsh.in:8000/upload_Aadhar_card_back',files = {'file':imageab.fileb}, verify=False)
            # d1 = eval(r1.json())
            d2 = eval(r2.json())
            d1 = eval(r1.json())
            
            return render(request, 'Aadharshow.html', {'formf':formf, 'formb':formb, 'image1':image1,'imageab':imageab,'d2':d2, 'd1':d1})

    else:
        formf = FUploadForm()
        formb = BUploadForm()
       

    return render(request, 'Aadhar.html', {'formf': formf, 'formb':formb})

############################ AADHAR CARD END ######################################


############################ PAN CARD #############################################

def pan(request):
    
    if request.method == 'POST':
        formp = PUploadForm(request.POST, request.FILES)
        if formp.is_valid():
            formp.save()
            image = formp.instance
            r = requests.post('https://devbankstatement.digisparsh.in:8000/upload_Pan_card',files = {'file':image.filep}, verify=False)
            d1 = eval(r.json())
            
            return render(request, 'panshow.html', {'formp':formp, 'image':image, 'd1':d1})

    else:
        formp = PUploadForm()
       

    return render(request, 'pan.html', {'formp': formp,})

############################ PAN CARD END ###########################################


############################ BANKSTATEMENT ##########################################

def bank(request):
    
    if request.method == 'POST':
        formb = BankForm(request.POST, request.FILES)
        if formb.is_valid():
            formb.save()
            data = formb.instance
          ######  response 
            url = "https://devbankstatement.digisparsh.in:8000/Bank_statement_Analysis/?"
            
            params={
                'text':data.text,
                'password': data.password
            }
            files ={
                'file' : data.statement
            }
            print(type(data.statement.file))
            
            r = requests.post(url,params=params,files=files ,verify=False)
           
           ####### response 

            response = eval(r.json())

            return render(request, 'statement.html', {'formb':formb, 'response':response})

            

    else:
        formb = BankForm()
       

    return render(request, 'bank.html', {'formb': formb,})
    


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


############################ BANKSTATEMENT END ########################################