from django import forms
from .models import Url
 
class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['url', 'keyword']
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center;', 'width':'100%', 'placeholder':'url을 입력하세요'}),
            'keyword': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center;', 'width':'100px', 'placeholder':'keyword를 입력하세요'}),
        }
