from django.contrib import admin
from . import models
from .models import articlepost, article_type,Research,groupmember
@admin.register(article_type)
class article_type(admin.ModelAdmin):
    list_display = ('id','type_name')
@admin.register(articlepost)
class articlepost(admin.ModelAdmin):
    list_display = ('title','author','article_type','created_time')
@admin.register(groupmember)
class groupmember(admin.ModelAdmin):
    list_display = ('name','grade','created_time')
admin.site.register(models.publication)
@admin.register(Research)
class Research(admin.ModelAdmin):
    list_display = ('title','created_time')