from django import forms
from .models import Evidence

class EvidenceForm(forms.ModelForm):
    upload=forms.FileField(label='첨부 파일', required=False,
                           widget=forms.FileInput(attrs={'class':'form'}))
    class Meta:
        model=Evidence
        fields=['title', 'content']
        exclude=['attached']