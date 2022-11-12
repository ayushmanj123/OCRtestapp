from django import forms
from django.forms import ModelForm
from .models import FUpload, BankStatement, BUpload, PUpload


class FUploadForm(ModelForm):
    class Meta:
        model = FUpload
        fields = ('filef',)

        labels = {
            'filef':'',
        }

class BUploadForm(ModelForm):
    class Meta:
        model = BUpload
        fields = ('fileb',)

        labels = {
            'fileb':'',
        }

class PUploadForm(ModelForm):
    class Meta:
        model = PUpload
        fields = ('filep',)

        labels = {
            'filep':'',
        }


class BankForm(ModelForm):
    class Meta:
        model = BankStatement

        fields = ('text','password','statement',)

        labels = {
            'text':'Bank Name',
            'password':'Password',
            'statement':'',
            
        }