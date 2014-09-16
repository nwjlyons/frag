from django import forms


class FragForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter a website address'}))
