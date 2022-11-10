import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms  import UploadForm, BankForm
from .models import Upload, BankStatement
from reportlab.pdfgen import canvas
import requests
import pdfkit
import base64

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
            
            return render(request, 'Adr_front.html', {'form':form, 'image':image, 'r':d1})

    else:
        form = UploadForm()
       

    return render(request, 'Adr_front.html', {'form': form,})
                

def aadharback(request):
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = form.instance
            
            img = Upload.objects.last()
            header= {
                "Content-Type": "application/json",
            }
            r = requests.post('https://devbankstatement.digisparsh.in:8000/upload_Aadhar_card_back',files = {'file':image.file}, verify=False)
            d1 = eval(r.json())
            
            return render(request, 'Adr_back.html', {'form':form, 'image':image, 'r':d1})

    else:
        form = UploadForm()
       

    return render(request, 'Adr_back.html', {'form': form,})
                
def pan(request):
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = form.instance
            
            img = Upload.objects.last()
            header= {
                "Content-Type": "application/json",
            }
            r = requests.post('https://devbankstatement.digisparsh.in:8000/upload_Pan_card',files = {'file':image.file}, verify=False)
            d1 = eval(r.json())
            
            return render(request, 'pan.html', {'form':form, 'image':image, 'r':d1})

    else:
        form = UploadForm()
       

    return render(request, 'pan.html', {'form': form,})



# def bank(request):
    
#     if request.method == 'POST':
#         formb = BankForm(request.POST, request.FILES)
#         if formb.is_valid():
#             formb.save()
#             data = formb.instance

#             img = BankStatement.objects.last()
#             header= {
#                 "Content-Type": "application/pdf",
#             }
#             r = requests.post('https://devbankstatement.digisparsh.in:8000/upload_file/?', params={'text': data.text, 'password':data.password} ,files={'file': data.statement}, headers=header, verify=False)
            
#             print(type(r))
#             print(r.status_code)
#             return render(request, 'bank.html', {'formb':formb, 'data':data, 'r':r})

#     else:
#         formb = BankForm()
       

#     return render(request, 'bank.html', {'formb': formb,})


def bank(request):
    
    if request.method == 'POST':
        formb = BankForm(request.POST, request.FILES)
        if formb.is_valid():
            formb.save()
            data = formb.instance
            
            url = "https://devbankstatement.digisparsh.in:8000/upload_file/?"
            # payload={}
            
            # files=[
            #         ('file',(data.statement,open(data.statement.url,'rb'),'application/pdf'))
            #         ]
            # headers= {
            #     "Content-Type": "application/pdf",
            # }
            params={
                'text':data.text,
                'password': data.password
            }
            files ={
                'file' : data.statement
            }
            print(type(data.statement.file))
            response = requests.post(url,params=params,files=files ,verify=False)
            # maindata = response.text.encode('utf-8')
            # print(response.text)
            
            # d1 = eval(f.json())
            # bytes = base64.b64decode(response.content)
            # with open('file.pdf', 'wb') as f:
            #     f.write(bytes)
            return render(request, 'statement.html', {'formb':formb, 'response':response})

            

    else:
        formb = BankForm()
       

    return render(request, 'bank.html', {'formb': formb,})
    

  

