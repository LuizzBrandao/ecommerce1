# forms.py
from django import forms

# Definindo as opções de quantidade de 1 a 20
QUANTIDADE_CHOICES = [(i, str(i)) for i in range(1, 21)]

class FormAdicionarProdutoCarrinho(forms.Form):
    # Campo para a quantidade, com opções de 1 a 20
    quantidade = forms.ChoiceField(
        choices=QUANTIDADE_CHOICES,
        initial='1',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Campo oculto para sobrepor a quantidade no carrinho, caso necessário
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput()
    )
