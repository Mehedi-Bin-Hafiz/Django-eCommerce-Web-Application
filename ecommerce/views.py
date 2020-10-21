from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django import forms
def home_page(request):
    context = {
        "title" : " Hello home",
        "content" : "This is homepage"
    }
    return  render(request, "home_page.html",context) #render is a shortcut that take a requst and return template file {} is a context

def about_page(request):
    context = {
        "title": " Hello about ",
        "content": "This is about page"
    }
    return  render(request, "home_page.html",context)

def contact_page(request):

    contact_form = ContactForm(request.POST or None) #it post then pass or not
    if contact_form.is_valid():

        print("Cleaned data",contact_form.cleaned_data)

    context = {
        "title": " Hello contact ",
        "content": "This is contact page",
        "form": contact_form
    }
    # if request.method ==  "POST":
        # print(request.POST.get("fullname"))
        # print(request.POST.get("email"))
        # print(request.POST.get("content"))
    return  render(request, "contact/view.html",context)

##validate
def clean_email(self):
    email = self.cleand_data.get('email')
    if not "@gmail.com" in email:
        raise forms.ValidationError("enter valid gmail")
    return email
