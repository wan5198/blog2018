# Generated by Django 2.0 on 2018-03-21 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180320_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pinlun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('author', models.CharField(max_length=50, verbose_name='评论人')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('email', models.CharField(max_length=50)),
                ('wenzhang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blogwenzhang', verbose_name='评论关联')),
            ],
        ),
    ]