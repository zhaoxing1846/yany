# Generated by Django 2.2.3 on 2019-08-23 11:48

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupwebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_time',),
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='photos_img', verbose_name='合照')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('reference', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='pub_img', verbose_name='配图')),
                ('abstract', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_time',),
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_time',),
            },
        ),
    ]
