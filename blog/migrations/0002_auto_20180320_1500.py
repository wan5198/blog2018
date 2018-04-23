# Generated by Django 2.0 on 2018-03-20 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='blogwenzhang',
            options={'verbose_name': '博文发布', 'verbose_name_plural': '博文发布'},
        ),
        migrations.AlterModelOptions(
            name='classify',
            options={'verbose_name': '文章分类', 'verbose_name_plural': '文章分类'},
        ),
        migrations.AlterField(
            model_name='blogwenzhang',
            name='amend_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改'),
        ),
        migrations.AlterField(
            model_name='blogwenzhang',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='blogwenzhang',
            name='classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Classify', verbose_name='文章分类'),
        ),
        migrations.AlterField(
            model_name='blogwenzhang',
            name='content',
            field=models.TextField(verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='blogwenzhang',
            name='release_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='blogwenzhang',
            name='title',
            field=models.CharField(max_length=100, verbose_name='文章标题'),
        ),
    ]
