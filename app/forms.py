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

        fields = ['text','password','statement']
        
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'input col-md-6', 'placeholder' : 'Bank Name'}),
            'email' : forms.EmailInput(attrs={'class': 'input col-md-6', 'placeholder' : 'Password'}),
            'statement': forms.FileInput(attrs={'type':'file', 'class':'form-control col-md-3', 'id':'inputGroupFile04', 'aria-describedby':'inputGroupFileAddon04', 'aria-label':'Upload', 'style':'margin-left:38%; margin-top:2%'})
        }