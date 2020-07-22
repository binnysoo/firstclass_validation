# Generated by Django 3.0.8 on 2020-07-21 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_validate', '0014_auto_20200721_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbase',
            name='birth',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ValidatedProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=200)),
                ('device', models.CharField(max_length=200)),
                ('age', models.SmallIntegerField()),
                ('blind', models.BooleanField(default=False)),
                ('coin', models.IntegerField(default=0)),
                ('birth', models.DateField(auto_now_add=True)),
                ('nick', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('area', models.IntegerField(choices=[(0, '서울'), (0, '경기'), (0, '인천'), (1, '강원'), (2, '충북'), (2, '세종'), (2, '충남'), (2, '대전'), (3, '경북'), (3, '대구'), (3, '울산'), (3, '부산'), (3, '경남'), (4, '전북'), (4, '전남'), (4, '광주'), (5, '제주'), (6, '해외')], default=0)),
                ('study', models.CharField(max_length=200)),
                ('height', models.IntegerField()),
                ('body', models.CharField(max_length=200)),
                ('drink', models.CharField(max_length=200)),
                ('smoke', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=200)),
                ('Character', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
