from django import forms
from django import forms
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Your title please'}))
    email = forms.EmailField()
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    'placeholder':'Your description please',
                                    'class':'new-class-name two',
                                    'id':'my-id-for-textarea',
                                    'rows':20,
                                    'cols':120
                                    }
                                )
                            )
    price = forms.DecimalField(initial=999.999)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self,*args,**kargs):
        title = self.cleaned_data.get('title')
        if 'CFE' in title:
            return title
        else:
            raise forms.ValidationError('this is not a valid title')

    def clean_email(self,*args,**kargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('this email is not valid')
        return email

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Your title please'}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    'placeholder':'Your description please',
                                    'class':'new-class-name two',
                                    'id':'my-id-for-textarea',
                                    'rows':20,
                                    'cols':120
                                    }
                                )
                            )
    price = forms.DecimalField(initial=999.999)