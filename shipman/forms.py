from django import forms

class TrackPackageForm(forms.Form):
  tracking_number = forms.CharField()
