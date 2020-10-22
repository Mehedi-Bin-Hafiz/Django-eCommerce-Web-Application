from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home_page(request):
    context = {
        "title" : " Hello home",
        "content" : "This is homepage"
    }
    if request.user.is_authenticated:
        context["premium"]="Thank you so much"
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
def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "title": " Hello User ",
        "content": "User login",
        "form": login_form
    }
    if login_form.is_valid():
        #print(request.user.is_authenticated)  #vvi is_authenticated() callable does not work
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request,username=username, password= password)
        if user is not None:
            print("user is loged in")
            login(request,user) # that login
            return redirect('/home')#it take user loginform
        else:
            print("error")
            raise forms.ValidationError("Username or password is not matching")
    # No backend authenticated the credentials
    return  render(request,"auth/login.html",context)
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "title": " Hello User ",
        "content": "User registration",
        "form": register_form
    }
    if register_form.is_valid():
        #print(request.user.is_authenticated)  #vvi is_authenticated() callable does not work
        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        password1 = register_form.cleaned_data.get('password1')
        email = register_form.cleaned_data.get('email')

        print(register_form.cleaned_data)


    # No backend authenticated the credentials
    return  render(request,"auth/register.html",context)
# def register_page(request):
#     form = LoginForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
#     return render(request,'auth/register.html',{})


##validate
def clean_email(self):
    email = self.cleand_data.get('email')
    if not "@gmail.com" in email:
        raise forms.ValidationError("enter valid gmail")
    return email
