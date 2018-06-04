from django import forms
from django.core import validators


class DataSubmission(forms.Form):
    name = forms.CharField()
    no_of_entries = forms.IntegerField()
    disk_space_required = forms.FloatField(validators=[validators.MaxValueValidator(500)])
    summary = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
