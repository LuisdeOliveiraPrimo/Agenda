from django.shortcuts import render, get_object_or_404, redirect
from contact.admin import *
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from contact.forms import *


def create(request):
    if request.method == 'POST':
            form = ContactForms(request.POST)
            context = {
                'form':form
            }

            if form.is_valid():
                  ...

            return render(
                request,
                'contact/create.html',
                context
            )  

    context = {
        'form':ContactForms()
        }

    return render(
        request,
        'contact/create.html',
        context
    )  