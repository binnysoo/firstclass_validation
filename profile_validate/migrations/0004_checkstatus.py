# Generated by Django 3.0.8 on 2020-07-18 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_validate', '0003_auto_20200718_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.CharField(max_length=200)),
                ('denied', models.CharField(max_length=200)),
            ],
        ),
    ]