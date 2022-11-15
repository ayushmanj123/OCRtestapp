from django import forms
from django.forms import ModelForm
from .models import FUpload, BankStatement, BUpload, PUpload, Resume


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
            'text' : forms.TextInput(attrs={'class': 'input col-md-2', 'placeholder' : 'Bank Name'}),
            'password' : forms.PasswordInput(attrs={ 'type':'password', 'class': 'input col-md-2 ', 'placeholder' : 'Password'}),
            'statement': forms.FileInput(attrs={'type':'file', 'class':'form-control col-md-2', 'id':'inputGroupFile04', 'aria-describedby':'inputGroupFileAddon04', 'aria-label':'Upload', 'style':'margin-left:41.5%; margin-top:2%'})
        }

class ResumeForm(ModelForm):
    class Meta:
        model = Resume

        fields = ['file',]
        
        widgets = {
            'file': forms.FileInput(attrs={'type':'file', 'class':'form-control col-md-2', 'id':'inputGroupFile04', 'aria-describedby':'inputGroupFileAddon04', 'aria-label':'Upload', 'style':'margin-left:41.5%; margin-top:2%'})
        }


