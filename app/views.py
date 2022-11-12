import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms  import FUploadForm, BUploadForm,BankForm, PUploadForm
from .models import BUpload, FUpload, BankStatement, PUpload
from reportlab.pdfgen import canvas
import requests
import pdfkit
import time
import os
import base64
import csv
from django.template.defaulttags import register
# Create your views here.

def home(request):
    return render(request, 'index.html')

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
            
            return render(request, 'Aadhar.html', {'formf':formf, 'formb':formb, 'image1':image1,'imageab':imageab,'d2':d2, 'd1':d1})

    else:
        formf = FUploadForm()
        formb = BUploadForm()
       

    return render(request, 'Aadhar.html', {'formf': formf, 'formb':formb})




                
def pan(request):
    
    if request.method == 'POST':
        formp = PUploadForm(request.POST, request.FILES)
        if formp.is_valid():
            formp.save()
            image = formp.instance
            r = requests.post('https://devbankstatement.digisparsh.in:8000/upload_Pan_card',files = {'file':image.filep}, verify=False)
            d1 = eval(r.json())
            
            return render(request, 'pan.html', {'formp':formp, 'image':image, 'd1':d1})

    else:
        formp = PUploadForm()
       

    return render(request, 'pan.html', {'formp': formp,})




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
            print("checking")
           
           ####### response 

            # HttpResponse(response.read(),content_type='application/pdf')


            # dir_path = os.path.dirname(os.path.realpath(__file__))
            # filename = f'C:/Users/user/Desktop/TestDjango/uploads/{data.text + ".pdf"}'
            # print(filename)
            # f = open(f'{filename}', 'wb')
            # # content = response.read()
         
            # f = f.write(response.text)
         
            # maindata = response.text.encode('utf-8')
            # print(response.text)
            
            # d1 = eval(f.json())
            # bytes = base64.b64decode(response.content)
            # with open('file.pdf', 'wb') as f:
            #     f.write(bytes)
            response = eval(r.json())
            # d1 = {'extracted_data': [{'date': 'Date', 'description': 'Narration', 'cheq_no': 'Chq./Ref.No.', 'debit': '', 'credit': '', 'balance': ''}, {'date': '02/11/21', 'description': 'UPI-RAKESH BABULAL GAGAN-8424847649@ Y BL-SBIN0012703-130624266290-PAY MENT FROM PHONE', 'cheq_no': '0000130624266290', 'debit': '7000.00', 'credit': '', 'balance': '8493.00'}, {'date': '02/11/21', 'description': 'UPI-PRASAD R BHANDA RKAR-9821674702@Y BL-CNRB0000033-130620105452-PAY MENT FROM PHONE', 'cheq_no': '0000130620105452', 'debit': '4500.00', 'credit': '', 'balance': '3993.00'}, {'date': '03/11/21', 'description': 'UPI-RAKESH BABULAL GAGAN-8424847649@ Y BL-IC1IC0000555-130768919976-PAY MENT FROM PHONE', 'cheq_no': '0000130768919976', 'debit': '', 'credit': '2000.00', 'balance': '5993.00'}, {'date': '05/11/21', 'description': 'ACH D- APHELION FINANCE-IHV CS9V NERZDHY', 'cheq_no': '0000006455266582', 'debit': '3889.00', 'credit': '', 'balance': '2104.00'}, {'date': '09/11/21', 'description': 'UPI-ALFALAH GRAIN AND GE-PAY TMQR2810050501011Q69Y BH99EHY @ PAY TM-PY TM0123456- 131365507742-PAY MENT FROM PHONE', 'cheq_no': '0000131365507742', 'debit': '186.00', 'credit': '', 'balance': '1918.00'}, {'date': '10/11/21', 'description': 'UPI-RAKESH BABULAL GAGAN-8424847649@ Y BL-IC1C0000555-131412918813-PAY MENT FROM PHONE', 'cheq_no': '0000131412918813', 'debit': '', 'credit': '1590.00', 'balance': '3508.00'}, {'date': '10/11/21', 'description': 'UPI-RAKESH BABULAL GAGAN-8424847649@ Y BL-SBIN0012703-131441962221-PAY MENT FROM PHONE', 'cheq_no': '0000131441962221', 'debit': '', 'credit': '6500.00', 'balance': '10008.00'}, {'date': '10/11/21', 'description': 'UPI-SHUBHAM SANJAY KHA PA-9822106435@ Y BL-IC1C0004111-131414776110-PAY MENT FROM PHONE', 'cheq_no': '0000131414776110', 'debit': '10000.00', 'credit': '', 'balance': '8.00'}, {'date': '30/11/21', 'description': 'GRESHMA FINVES-SALRGOO1', 'cheq_no': '0000111301056653', 'debit': '', 'credit': '19050.00', 'balance': '19058.00'}, {'date': '30/11/21', 'description': 'UPI-RAKESH BABULAL GAGAN-8424847649@ Y BL-ICIC0000555-133467090765-PAY MENT FROM PHONE', 'cheq_no': '0000133467090765', 'debit': '6000.00', 'credit': '', 'balance': '13058.00'}], 'KPI': {'opening_balance': '15493.0', 'closing_balance': '13058.0', 'average_balance': '6814.1', 'credit_sum': '58280.0', 'debit_sum': '63150.0', 'debit_to_credit_ratio': '1.08:1', 'three_month_debit_average': "['Nov value is 63150.0']", 'three_month_credit_average': "['Nov value is 58280.0']", 'three_month_debit_to_credit_ratio': '1.08:1', 'three_month_avg_balance': "['Nov value is 6814.1']", 'heighest_debits': '10/11/21 amount is 10000.0', 'heighest_credits': '30/11/21 amount is 19050.0', 'identical_debit_credit': 'No identical Credit-Debit', 'eod': 'No EOD Balance', 'very_high_credit': 'No High credit', 'very_high_debit': 'No High debit', 'Ac holder name': 'MR RAKESH BABULAL GAGANWAD', 'account number': '90100388834580', 'start end date': 'From 2021-02-11 to 2021-11-30', 'bank name': 'HDFC', 'post_salary_payout': '2021-10-11 00:00:00', 'amount_tallying_inconsistancy': 'No tallying inconsistancy', 'highest_balance': '19058.0', 'lowest_balance': '8.0', 'highest_credit_balance': '19050.0', 'highest_debit_balance': '10000.0'}}
            # maindata = response['extracted_data']
            
          
            # data_file = open('data_file.csv', 'w')
            # csv_writer = csv.writer(data_file)
            # count = 0
            # for d in maindata:
            #     if count == 0:
            #         header = d.keys()
            #         csv_writer.writerow(header)
            #         count+=1
            # csv_writer.writerow(d.values())
            # data_file.close()
            # response = d1
            return render(request, 'statement.html', {'formb':formb, 'response':response})

            

    else:
        formb = BankForm()
       

    return render(request, 'bank.html', {'formb': formb,})
    


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

