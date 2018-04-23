# Generated by Django 2.0 on 2018-03-23 12:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180322_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guanggaoimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='图片名字')),
                ('guanggao_img', models.ImageField(upload_to='index_img', verbose_name='上传图片')),
            ],
            options={
                'verbose_name': '广告图管理',
                'verbose_name_plural': '广告图管理',
            },
        ),
        migrations.CreateModel(
            name='Lunbotu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='图片名字')),
                ('index_img', models.ImageField(upload_to='index_img', verbose_name='上传图片')),
            ],
            options={
                'verbose_name': '轮播图管理',
                'verbose_name_plural': '轮播图管理',
            },
        ),
        migrations.AlterField(
            model_name='blogwenzhang',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='文章内容'),
        ),
    ]
