from django import forms
from .models import TaxReturn

class TaxReturnForm(forms.ModelForm):
    class Meta:
        model = TaxReturn
        fields = ['financial_year', 'salary_income', 'other_income']
        widgets = {
            'salary_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'other_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'financial_year': forms.TextInput(attrs={'class': 'form-control'}),
        }