from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context = {
        "title" : " Hello Mehedi"
    }
    return  render(request, "home_page.html",context) #render is a shortcut that take a requst and return template file {} is a context

def about_page(request):
    context = {
        "title": " Hello about "
    }
    return  render(request, "home_page.html",context)

def contact_page(request):
    context = {
        "title": " Hello contact "
    }
    return  render(request, "home_page.html",context)
