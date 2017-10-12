from django.shortcuts import render_to_response
from django.http import HttpResponse
from micropost.models import MicroPost

def home(request):
    latest_micropost_list = MicroPost.objects.filter(display=True)
    return render_to_response('home.html',{'latest_micropost_list':latest_micropost_list})
