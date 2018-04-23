# Generated by Django 2.0 on 2018-03-29 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20180328_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_EX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='static/avatar')),
                ('bj', models.CharField(default='blog_2018', max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户头像管理',
                'verbose_name_plural': '用户头像管理',
            },
        ),
        migrations.AddField(
            model_name='pinlun',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='评论关联'),
            preserve_default=False,
        ),
    ]
