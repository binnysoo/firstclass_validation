# Generated by Django 3.0.8 on 2020-07-22 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_validate', '0016_auto_20200722_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validatedprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_validate.UserBase'),
        ),
    ]
