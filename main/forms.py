from django import forms
from froala_editor.widgets import FroalaEditor

class PageForm(forms.ModelForm):
  content = forms.CharField(widget=FroalaEditor)
  
class SubmitForm(forms.Form):
	name = forms.CharField(label='Your Name', max_length=200)
	email = forms.EmailField(label='Your Email', max_length=254)
	title = forms.CharField(label='Title', max_length=200)
	file = forms.FileField(label='Upload Your Story')