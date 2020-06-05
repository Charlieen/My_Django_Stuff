from django import forms
from django.core import validators

class FormUser(forms.Form):
    first_name = forms.CharField(label="First Name:")
    last_name = forms.CharField(label ="Last Name:")
    email = forms.EmailField(label="Your Email:")

    def clean(self):
        all_clean_data = super().clean()
        first_name = all_clean_data['first_name']
        print(first_name)
        
        if len(first_name) < 4:
            raise forms.ValidationError('First Name must great then four letters!')
        print(all_clean_data)

