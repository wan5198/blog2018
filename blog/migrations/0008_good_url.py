# Generated by Django 2.0 on 2018-03-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180323_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='网站名字')),
                ('gurl', models.CharField(max_length=100, verbose_name='跳转网址')),
                ('miaosu', models.CharField(max_length=200, verbose_name='描述说明')),
            ],
            options={
                'verbose_name': '友情链接管理',
                'verbose_name_plural': '友情链接管理',
            },
        ),
    ]