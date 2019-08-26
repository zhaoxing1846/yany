from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Prof(models.Model):
    Img = models.ImageField(upload_to='prof_photo', null=True, blank=True, verbose_name='头像')
    Name =  models.CharField(max_length=50)
    Brief =  RichTextUploadingField()
    Detail = RichTextUploadingField()

    def __str__(self):
        return self.Name

class Member_type(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

class Member(models.Model):
    Name = models.CharField(max_length=50)
    Member_type = models.ForeignKey(Member_type, on_delete=models.DO_NOTHING)
    Img = models.ImageField(upload_to='peo_img', null=True, blank=True, verbose_name='照片')
    Email = models.CharField(max_length=50)
    Created_time = models.DateTimeField(auto_now_add=True)
    Introduction = models.TextField()

    class Meta:
        ordering = ('-Created_time',)
    def __str__(self):
        return self.Name

class Research(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_time',)
    def __str__(self):
        return self.title

class publication(models.Model):
    title = models.CharField(max_length=200)
    reference = models.TextField()
    img = models.ImageField(upload_to='pub_img', null=True, blank=True, verbose_name='配图')
    abstract = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

class news(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title


class Photos(models.Model):
    img = models.ImageField(upload_to='photos_img', null=True, blank=True, verbose_name='合照')
    title = models.CharField(max_length=500)
class Contact(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    def __str__(self):
        return self.title

class Carousel(models.Model):
    number = models.IntegerField('编号', help_text='编号决定图片播放的顺序，图片不要多于5张')
    title = models.CharField('标题', max_length=20, blank=True, null=True, help_text='标题可以为空')
    content = models.CharField('描述', max_length=80)
    img = models.ImageField(upload_to='index_img', null=True, blank=True, verbose_name='首页配图')
    class Meta:
        verbose_name = '图片轮播'
        verbose_name_plural = verbose_name
        # 编号越小越靠前，添加的时间约晚约靠前
        ordering = ['number', '-id']

    def __str__(self):
        return self.content[:25]

class indeximage(models.Model):
    img = models.ImageField(upload_to='index_img', null=True, blank=True, verbose_name='首页图')
    content = RichTextUploadingField()

    def __str__(self):
        return self.content[:10]