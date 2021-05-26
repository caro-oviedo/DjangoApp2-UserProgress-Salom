from django import forms
from .models import *
from django.contrib.auth.models import User

class CompleteTrick(forms.ModelForm):
    complete =forms.BooleanField()

    class Meta:
        model = Done 
        fields = ['complete']

