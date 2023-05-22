from django import forms
from .models import *


# class SubscriberForm(forms.ModelForm):
#
#   class Meta:
#      model = Subscriber
#     exclude = [""]

class FeedbackForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(required=True)
    date = forms.DateField(widget=forms.SelectDateWidget, required=True)
