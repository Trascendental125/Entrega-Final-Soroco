from django import forms
from . import models


class SegurosCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.SegurosCategoria
        fields = "__all__"


class SegurosForm(forms.ModelForm):
    class Meta:
        model = models.Seguros
        fields = "__all__"