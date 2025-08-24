from django import forms
from .models import Marker

class MarkerUploadForm(forms.ModelForm):
    class Meta:
        model = Marker
        fields = ['src_img']  # input only source image

class MarkerEditForm(forms.ModelForm):
    class Meta:
        model = Marker
        fields = '__all__'  # offer everything for edit



