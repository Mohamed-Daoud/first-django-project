from django.http import HttpResponse # send response to user
from django.shortcuts import render  # to render templates

def homepage(request):
    # return HttpResponse ('homepage is the landing page')
    return render(request, 'homepage.html') #django knows to look under templates


def about(request):
    # return HttpResponse('About Us as you would expect')
    return render(request, 'about.html')
