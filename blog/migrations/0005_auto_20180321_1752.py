# Generated by Django 2.0 on 2018-03-21 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_pinlun'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogwenzhang',
            options={'ordering': ['-release_time'], 'verbose_name': '博文发布', 'verbose_name_plural': '博文发布'},
        ),
    ]
