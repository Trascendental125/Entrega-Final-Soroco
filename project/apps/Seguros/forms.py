from django import forms
from . import models


class SeguroCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.SeguroCategoria
        fields = "__all__"


class SeguroForm(forms.ModelForm):
    class Meta:
        model = models.Seguro
        fields = "__all__"