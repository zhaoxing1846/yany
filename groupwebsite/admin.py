from django.contrib import admin
from .models import Prof,Member_type,Member,news,Research,Photos,publication,Contact,Carousel,indeximage
# Register your models here.

admin.site.site_header = 'Yan Research Group'
admin.site.site_title = '后台管理'
@admin.register(Prof)
class Prof(admin.ModelAdmin):
    list_display = ('Name',)

@admin.register(Member_type)
class Member_type(admin.ModelAdmin):
    list_display = ('type_name',)

@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display = ('Name','Member_type','Created_time')

@admin.register(news)
class news(admin.ModelAdmin):
    list_display = ('title','created_time')

@admin.register(Research)
class Research(admin.ModelAdmin):
    list_display = ('title','created_time')

@admin.register(Photos)
class Photos(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(publication)
class publication(admin.ModelAdmin):
    list_display = ('title','created_time')

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('number', 'title')

@admin.register(indeximage)
class indeximage(admin.ModelAdmin):
    list_display = ('content',)