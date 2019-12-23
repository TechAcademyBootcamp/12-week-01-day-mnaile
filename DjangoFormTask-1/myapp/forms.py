from django import forms
from .models import Login, Admin
    
    # OldContactForm class'in adini deyishib ContactForm yazib 1-ci task'i yoxlamaq olar
    
class OldContactForm(forms.Form):

    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                        'id': 'inputEmail4',
                                        'class': 'form-control',
                                        'placeholder':'Email',
                                    }))
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={
                                        'id': 'inputPassword4',
                                        'class': 'form-control',
                                        'placeholder':'Password',
                                    }))
    address = forms.CharField(label='Address',
                                widget=forms.TextInput(attrs={
                                        'id': 'inputAddress',
                                        'class': 'form-control',
                                        'placeholder':'1234 Main St',
                                    }))
    address_2 = forms.CharField(label='Address 2',
                                widget=forms.TextInput(attrs={
                                        'id': 'inputAddress2',
                                        'class': 'form-control',
                                        'placeholder':'Apartment, studio, or floor',
                                    }))
    city = forms.CharField(label='City',
                            widget=forms.TextInput(attrs={
                                'id':'inputCity',
                                'class': 'form-control',
                            }))
    state = forms.ChoiceField(label='State',
                                 widget=forms.Select(attrs={
                                'id': 'inputState',
                                'class': 'form-control',
                                    }))
    zip = forms.CharField(label='Zip',
                            widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'inputZip',
                                    }))
    check = forms.BooleanField(initial=False, 
                                widget=forms.CheckboxInput(attrs={
                                    'id':'gridCheck',
                                    'class':'form-check-input',
                                }))


class ContactForm(forms.ModelForm):
    admin = forms.CharField(label='Admin',
                            widget=forms.Select(attrs={
                                'class': 'form-control',
                            }))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                        'id': 'inputEmail4',
                                        'class': 'form-control',
                                        'placeholder':'Email',
                                    }))
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={
                                        'id': 'inputPassword4',
                                        'class': 'form-control',
                                        'placeholder':'Password',
                                    }))
    address = forms.CharField(label='Address',
                                widget=forms.TextInput(attrs={
                                        'id': 'inputAddress',
                                        'class': 'form-control',
                                        'placeholder':'1234 Main St',
                                    }))
    address_2 = forms.CharField(label='Address 2',
                                widget=forms.TextInput(attrs={
                                        'id': 'inputAddress2',
                                        'class': 'form-control',
                                        'placeholder':'Apartment, studio, or floor',
                                    }))
    city = forms.CharField(label='City',
                            widget=forms.TextInput(attrs={
                                'id':'inputCity',
                                'class': 'form-control',
                            }))
    state = forms.ChoiceField(label='State',
                                 widget=forms.Select(attrs={
                                'id': 'inputState',
                                'class': 'form-control',
                                    }))
    zip = forms.CharField(label='Zip',
                            widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'inputZip',
                                    }))
    check = forms.BooleanField(initial=False, 
                                widget=forms.CheckboxInput(attrs={
                                    'id':'gridCheck',
                                    'class':'form-check-input',
                                }))

    class Meta:
        model = Login
        fields = (
            'admin',
            'email',
            'password',
            'address',
            'address_2',
            'city',
            'state',
            'zip',
            'check',
        )