# Generated by Django 2.2.3 on 2019-08-23 06:29

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(blank=True, null=True, upload_to='prof_photo', verbose_name='头像')),
                ('Name', models.CharField(max_length=50)),
                ('Brief', ckeditor_uploader.fields.RichTextUploadingField()),
                ('Detail', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Img', models.ImageField(blank=True, null=True, upload_to='peo_img', verbose_name='照片')),
                ('Email', models.CharField(max_length=50)),
                ('Created_time', models.DateTimeField(auto_now_add=True)),
                ('Introduction', models.TextField()),
                ('Member_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='groupwebsite.Member_type')),
            ],
            options={
                'ordering': ('-Created_time',),
            },
        ),
    ]
