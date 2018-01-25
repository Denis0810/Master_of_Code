from django import forms


class ZIPForms(forms.Form):
    zip_code = forms.DecimalField(max_digits=5,decimal_places=0)
    content = forms.TextInput()

