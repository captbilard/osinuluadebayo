from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.
def index(request):
    form = ContactForm()
    return render(request, "adebayo_osinulu/index.html", {'form':form})

def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # fname = form.cleaned_data['First_Name']
            # lname = form.cleaned_data['Last_Name']
            # from_email = form.cleaned_data['Email']
            # phone_number = form.cleaned_data['Phone_Number']
            # message = form.cleaned_data['Message']

            # subject = f"{fname} {lname} wants to interact with you. You can reach him on {phone_number}"
            # recipients= ['osinluadebayo@gmail.com','bilardosinulu@gmail.com']
            return redirect('index' )
    else:
        form = ContactForm()
        return render(request, "adebayo_osinulu/index.html", {'form':form})
