from django import forms
from django.forms import ModelForm
from .models import Upload, BankStatement


class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('file',)

        labels = {
            'file':'File',
        }

class BankForm(ModelForm):
    class Meta:
        model = BankStatement

        fields = ('text','password','statement',)

        labels = {
            'text':'',
            'password':'',
            'statement':'',
        }