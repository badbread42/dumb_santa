from django import forms
from .models import dumb_santa

class dumb_santa_form(forms.ModelForm):
	address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'denchik@rencap.com'}), required=True)
	extends = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'увлечения, хобби, тайные желания'}), required=True)

	class Meta:
		model = dumb_santa
		fields = ('address', 'extends',)