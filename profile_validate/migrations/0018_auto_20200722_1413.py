# Generated by Django 3.0.8 on 2020-07-22 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_validate', '0017_auto_20200722_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautyscore',
            name='scored_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giver', to='profile_validate.UserBase'),
        ),
        migrations.AlterField(
            model_name='beautyscore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='profile_validate.UserBase'),
        ),
    ]
