from django.shortcuts import render_to_response, get_object_or_404
from website.models import articlepost

def home(request):
    context = {}
    context['articles'] = articlepost.objects.all()[:10]
    return render_to_response('home.html',context)
