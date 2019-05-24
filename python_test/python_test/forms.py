from django import forms
from .models import Client


class ClientAddForm(forms.ModelForm):
    street_name = forms.CharField(required=False)
    suburb = forms.CharField(required=False)
    postcode = forms.CharField(required=False)
    state = forms.CharField(required=False)
    client_contact_name = forms.CharField(required=True)

    class Meta:
        model = Client
        fields = ('client_name', 'street_name', 'suburb', 'postcode', 'state', 'client_contact_name', 'email',
                  'phone_number',)
