from django.shortcuts import render_to_response
from django.http import HttpResponse
from micropost.models import MicroPost
from django.template import RequestContext, loader
import logging

def index(request):
    latest_micropost_list = MicroPost.objects.all().order_by('-pub_date')[:5]
    return render_to_response('micropost/index.html',{'latest_micropost_list':latest_micropost_list})

def detail(request, micro_post_id):
    try:
        mp = MicroPost.objects.get(pk=micro_post_id)
    except MicroPost.DoesNotExist:
        raise Http404
    return render_to_response('micropost/detail.html', {'micro_post': mp})

def create(request):
    logging.warn('Bug Submitted By User: {} Description: {}'.format(request.user, request.POST['bug_description']))
    return HttpResponse('Bug successfully submitted, thanks!')