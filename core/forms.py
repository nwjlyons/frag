from django import forms


class FragForm(forms.Form):
    url = forms.URLField()
