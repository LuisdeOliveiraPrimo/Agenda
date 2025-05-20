from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from . import models



class ContactForms(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe a',
                'placeholder': 'Digite Aqui'
            }
        ),
        label='Primeiro nome',
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe a',
                'placeholder': 'Digite Aqui',
            }
        ),
        label='Sobrenome',
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe a',
                'placeholder': 'Número',
            }
        ),
        label='Telefone',
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe a',
                'placeholder': 'Email',
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'classe a',
                'placeholder': 'Texto.',
            }
        ),
        label='Descrição',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name','phone','email','description','category',
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        phone = cleaned_data.get('phone') 

        if first_name == last_name:
            msg = ValidationError(
                'Seu nome não pode ser igual ao seu sobrenome.',
                code='invalid'
            )
            self.add_error('last_name', msg)

        if first_name and len(first_name) < 2:
            msg = ValidationError(
                'Nome deve ter pelo menos 2 caracteres.',
                code='invalid'
            )
            self.add_error('first_name', msg)

        for x in phone:
            if not x.isdigit():
                msg = ValidationError(
                    'Número de telefone inválido.',
                    code='invalid'
                )
                self.add_error('phone', msg)



        


