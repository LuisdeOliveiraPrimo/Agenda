from django.shortcuts import render, redirect
from django.urls import reverse
from contact.admin import *
from contact.forms import *


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
            form = ContactForms(request.POST)
            context = {
                'form':form,
                'form_action':form_action
            }

            if form.is_valid():
                contact = form.save()
                return redirect('contact:update', Contact_id=contact.id)


            return render(
                request,
                'contact/create.html',
                context
            )  

    context = {
        'form':ContactForms(),
        'form_action':form_action
    }
    return render(
        request,
        'contact/create.html',
        context
    )  

def update(request, contact_id):
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
            form = ContactForms(request.POST)
            context = {
                'form':form,
                'form_action':form_action
            }

            if form.is_valid():
                contact = form.save()
                return redirect('contact:update', Contact_id=contact.id)


            return render(
                request,
                'contact/create.html',
                context
            )  

    context = {
        'form':ContactForms(),
        'form_action':form_action
    }
    return render(
        request,
        'contact/create.html',
        context
    )  