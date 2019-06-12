from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Message']
        widgets = {
            'First_Name': forms.TextInput(
                attrs={'class':'form-control', 'name':'name', 'placeholder':'Firstname *', 'required':'required'}
            ),
            'Last_Name' : forms.TextInput(
                attrs={'class':'form-control', 'name':'surname', 'placeholder':'Lastname *', 'required':'required'}
            ),
            'Email': forms.EmailInput(
                attrs={'class':'form-control', 'name':'phone', 'placeholder':'Email *',}
            ),
            'Phone_Number':forms.TextInput(
                attrs={'class':'form-control', 'name':'phone', 'placeholder':'Phone number',}
            ),
            'Message': forms.Textarea(
                attrs={'class':'form-control', 'name':'message', 'placeholder':'Message for me *', 'rows':4, 'required':'required'}
            )
        }