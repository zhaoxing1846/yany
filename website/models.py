from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.
class article_type(models.Model):
    type_name = models.CharField(max_length=20)
    def __str__(self):
       return self.type_name
class articlepost(models.Model):
    title = models.CharField(max_length=50)
    article_type = models.ForeignKey(article_type,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

class publication(models.Model):
    title = models.CharField(max_length=200)
    reference = models.TextField()
    img = models.ImageField(upload_to='static/pub_img', null=True, blank=True, verbose_name='配图')
    abstract = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

class groupmember(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    created_time =models.DateTimeField(auto_now_add=True)
    introduction = models.TextField()
    img = models.ImageField(upload_to='static/peo_img',null=True,blank=True,verbose_name='头像')
    class Meta:
       ordering = ('-created_time',)
    def __str__(self):
       return self.name

class Research(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title