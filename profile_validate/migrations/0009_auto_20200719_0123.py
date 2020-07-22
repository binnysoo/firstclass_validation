# Generated by Django 3.0.8 on 2020-07-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_validate', '0008_auto_20200719_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstatus',
            name='reason',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='flag_type',
            field=models.IntegerField(choices=[(0, 'basic_profile'), (1, 'profile_photo'), (2, 'paper'), (3, 'beauty'), (4, 'noFilter')], default=0),
        ),
    ]