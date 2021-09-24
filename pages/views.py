from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(args , kwargs)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html",{})

def contact_view(request, *arg,**kwargs):
    #return HttpResponse("<h1>Contact page</h1>")
    return render(request,"contact.html",{})

def about_view(request, *arg,**kwargs):
    my_context = {
        "my_text": "This is about me",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hello World</h1>",
    }
    return render(request,"about.html",my_context)

def social_view(*arg,**kwargs):
    return HttpResponse("<h1>Social page</h1>")