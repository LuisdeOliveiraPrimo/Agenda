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
        help_text='Troque o seu sobrenome',
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

    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name','phone','email','description','category',
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Seu nome não poded ser igual a o seu sobrenome',
                code='invalid'
            )
            self.add_error('last_name', msg)

    # def clean_last_name(self):
    #     last_name = self.cleaned_data.get('last_name')

    #     if last_name == 'first_name':
    #         self.add_error(
    #             'first_name',
    #             ValidationError(
    #                 'Seu primeiro nome não pode ser igual a o segundo.',
    #                 code='Invalid'
    #             )
    #         )
            
    #     return last_name