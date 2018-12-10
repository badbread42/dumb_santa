from django import forms
from .models import dumb_santa

class dumb_santa_form(forms.ModelForm):
	address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'iwilldonatyou@rencap.com'}))
	extends = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'алергии, неприязнь, нетерпимости'}))

	class Meta:
		model = dumb_santa
		fields = ('address', 'extends',)