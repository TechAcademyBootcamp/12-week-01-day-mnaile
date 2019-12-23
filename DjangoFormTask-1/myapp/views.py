from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    context = {'form' : ContactForm()}
    return render (request, 'form.html', context)
