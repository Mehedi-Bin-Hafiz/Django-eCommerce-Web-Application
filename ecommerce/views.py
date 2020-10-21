from django.shortcuts import render
from django.http import HttpResponse

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
    context = {
        "title": " Hello contact ",
        "content": "This is contact page"
    }
    return  render(request, "home_page.html",context)
