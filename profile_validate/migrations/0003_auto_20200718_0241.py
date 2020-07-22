# Generated by Django 3.0.8 on 2020-07-17 17:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profile_validate', '0002_useradmin_userstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstatus',
            old_name='profile_face',
            new_name='flag',
        ),
        migrations.RemoveField(
            model_name='userstatus',
            name='profile_info',
        ),
        migrations.RemoveField(
            model_name='userstatus',
            name='profile_paper',
        ),
        migrations.RemoveField(
            model_name='userstatus',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='userstatus',
            name='profile_real',
        ),
        migrations.AddField(
            model_name='userbase',
            name='age',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbase',
            name='blind',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userbase',
            name='coin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userbase',
            name='device',
            field=models.CharField(default='android', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbase',
            name='joined_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbase',
            name='joined_type',
            field=models.CharField(default='서류인증', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userstatus',
            name='admin',
            field=models.CharField(default='김란이 주임', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userstatus',
            name='flag_type',
            field=models.IntegerField(choices=[(0, 'basic_profile'), (1, 'profile_photo'), (2, 'val_paper'), (3, 'val_beauty'), (4, 'val_noFilter')], default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_validate.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userinterview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_validate.UserProfile'),
        ),
        migrations.AlterField(
            model_name='usermark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_validate.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='area',
            field=models.IntegerField(choices=[(0, '서울'), (0, '경기'), (0, '인천'), (1, '강원'), (2, '충북'), (2, '세종'), (2, '충남'), (2, '대전'), (3, '경북'), (3, '대구'), (3, '울산'), (3, '부산'), (3, '경남'), (4, '전북'), (4, '전남'), (4, '광주'), (5, '제주'), (6, '해외')], default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_validate.UserBase'),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_validate.UserBase'),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_validate.UserProfile'),
        ),
        migrations.DeleteModel(
            name='UserAdmin',
        ),
    ]