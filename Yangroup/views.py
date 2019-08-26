from django.shortcuts import render_to_response, get_object_or_404
from groupwebsite.models import Carousel, news,publication,indeximage

def Home(request):
    context = {}
    list1=context['indexallnews'] = news.objects.all()
    list2=context['indexallpubs'] = publication.objects.all()
    if len(list1)>5:
       context['indexnews'] = news.objects.all()[:5]
    else:
        context['indexnews'] = news.objects.all()
    if len(list2)>5:
        context['indexpubs'] = publication.objects.all()[:5]
    else:
        context['indexpubs'] = publication.objects.all()
    context['carousels'] = Carousel.objects.all()
    context['carousel1'] =Carousel.objects.all()[0]
    context['carousel2'] = Carousel.objects.all()[1]
    context['carousel3'] = Carousel.objects.all()[2]
    context['carousel4'] = Carousel.objects.all()[3]
    context['indeximage'] =indeximage.objects.all()[0]
    return render_to_response('Home.html',context)