# Generated by Django 2.0 on 2018-03-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180320_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recommended',
            options={'verbose_name': '置顶消息', 'verbose_name_plural': '置顶消息'},
        ),
        migrations.AddField(
            model_name='blogwenzhang',
            name='reads',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recommended',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='recommended',
            name='title',
            field=models.CharField(max_length=100, verbose_name='置顶标题'),
        ),
    ]
