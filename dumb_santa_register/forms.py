from django import forms
from .models import dumb_santa

class dumb_santa_form(forms.ModelForm):

	class Meta:
        model = dumb_santa
        fields = ('address', 'extends',)