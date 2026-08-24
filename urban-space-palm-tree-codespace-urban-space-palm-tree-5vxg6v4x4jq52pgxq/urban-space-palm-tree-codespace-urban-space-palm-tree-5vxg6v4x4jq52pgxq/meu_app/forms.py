from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "numero_patrimonio", "tipo", "em_uso"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex.: Notebook Dell Latitude",
            }),
            "numero_patrimonio": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ex.: 1001",
                "min": "1",
            }),
            "tipo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex.: Notebook, Monitor, Impressora",
            }),
            "em_uso": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }
        labels = {
            "nome": "Nome do equipamento",
            "numero_patrimonio": "Número de patrimônio",
            "tipo": "Tipo",
            "em_uso": "Equipamento em uso",
        }


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "seu@email.com"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {"username": "Nome de usuário"}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escolha um usuário"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Crie uma senha"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Repita a senha"})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
