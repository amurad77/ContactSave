from django.shortcuts import render
from core.forms import ContactForm

# Create your views here.

# def home(request):
#     return render(request, 'test.html')



def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = ContactForm(data=contact_data)
        if form.is_valid():
            form.save()
            print('Form save')
        else:
            print('Form is invalid')
    context = { 
        'form':form
    }
    return render(request, 'test.html', context)
