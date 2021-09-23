from django import forms

from core.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'number',
            'email',
            'subject',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                                    'class': 'user-box',
                                    
                                }),
            'last_name': forms.TextInput(attrs={
                                    'class': 'user-box',
                                    'id': 'form'
                                    
                                }),
            'number': forms.TextInput(attrs={
                                    'class': 'user-box',
                                    'id': 'form'
                                }),
            'email': forms.EmailInput(attrs={
                                    'class': 'user-box',
                                    'id': 'form'
                                }),
            'subject': forms.TextInput(attrs={
                                    'class': 'user-box',
                                    'id': 'form'
                                }),
        }



    # first_name = forms.CharField(max_length=40, label='First name')
    # last_name = forms.CharField(max_length=40, label='Last name')
    # number = forms.CharField(max_length=15, label='Number')
    # email = forms.CharField(max_length=40, label='Email')
    # subject = forms.CharField(max_length=50, label='Subject')