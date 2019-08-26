from django.shortcuts import render_to_response, get_object_or_404
from .models import Prof, Member_type, Member,Research,Photos,news,publication,Contact
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def Professor(request):
    context = {}
    context['Professors'] = Prof.objects.all()
    return render_to_response('Professor.html', context)
def Type(request):
    context = {}
    People_type = Member_type.objects.all()
    context['Members'] = Member.objects.all()
    context['People_types'] = People_type
    return render_to_response('People.html', context)

def news_list(request):
    context = {}
    news_list = news.objects.all()
    context['all'] = news_list
    paginator = Paginator(news_list, 10)
    page = request.GET.get('page')
    context ['news'] = paginator.get_page(page)
    return render_to_response('news.html',context)

def news_detail(request,id):
    context = {}
    context ['new'] = get_object_or_404(news,id=id)
    return render_to_response('new.html',context)

def research(request):
    context = {}
    context['researches'] = Research.objects.all()
    return render_to_response('research.html', context)

def publications_list(request):
    context = {}
    context ['publications']= publication.objects.all()
    return render_to_response('publications.html',context)

def Ourphotos(request):
    context={}
    context['ourphotos']=Photos.objects.all()
    return render_to_response('Photos.html', context)

def contact(request):
    context = {}
    context['contacts'] = Contact.objects.all()
    return render_to_response('Contact.html', context)

def search(request):
    context = {}
    search_info = request.GET.get('search_info')
    error_msg = ""
    context['search_info']=search_info
    if not search_info:
        error_msg = "您需要输入想要搜索的内容"
        return render_to_response('search_results.html', context)
    search_result = news.objects.filter(Q(title__icontains=search_info)|Q(content__icontains=search_info))
    context['search_results'] = search_result
    return render_to_response('search_results.html', context)