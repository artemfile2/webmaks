# Generated by Django 2.0.7 on 2018-09-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_allfiles_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissio'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDbf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/dbf/')),
            ],
        ),
    ]
