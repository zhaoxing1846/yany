from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import article_type, articlepost,publication,groupmember,Research
# Create your views here.
def article_list(request):
    context = {}
    article_list = articlepost.objects.all()
    context['all'] = article_list
    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    context ['articles'] = paginator.get_page(page)
    return render_to_response('list.html',context)
def article_detail(request,id):
    context = {}
    context ['article'] = get_object_or_404(articlepost,id=id)
    return render_to_response('detail.html',context)
def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(article_type, pk=blog_type_pk)
    context['articles'] = articlepost.objects.filter(article_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blogs_with_type.html', context)
def uploadimage(request,id):
    context = {}
    context['images'] = uploadimage.objects.all()
    context['image'] = get_object_or_404(uploadimage, id=id)


def publication_list(request):
    context = {}
    context ['publications']= publication.objects.all()
    return render_to_response('publication.html',context)

def member_list(request):
    context = {}
    context ['members']= groupmember.objects.all()
    return render_to_response('member.html',context)
def research(request):
    context = {}
    context['researches'] = Research.objects.all()
    return render_to_response('research.html', context)
