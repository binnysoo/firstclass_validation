# Generated by Django 3.0.8 on 2020-07-20 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_validate', '0013_beautyscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautyscore',
            name='scored_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='beautyscore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
