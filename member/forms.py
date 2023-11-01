from django import forms
class PostForm(forms.Form):
    name = forms.CharField()
    img = forms.FileField(label="description")
    