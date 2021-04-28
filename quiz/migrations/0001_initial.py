# Generated by Django 3.1.7 on 2021-04-28 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.IntegerField()),
                ('firstExample', models.CharField(blank=True, max_length=2000)),
                ('secondExample', models.CharField(blank=True, max_length=2000)),
                ('thirdExample', models.CharField(blank=True, max_length=2000)),
                ('fourthExample', models.CharField(blank=True, max_length=2000)),
                ('firstCommentary', models.CharField(blank=True, max_length=2000)),
                ('secondCommentary', models.CharField(blank=True, max_length=2000)),
                ('thirdCommentary', models.CharField(blank=True, max_length=2000)),
                ('fourthCommentary', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='VersionCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('android_version', models.CharField(blank=True, max_length=1000)),
                ('android_msg', models.CharField(blank=True, max_length=1000)),
                ('android_status', models.CharField(blank=True, max_length=1000)),
                ('ios_version', models.CharField(blank=True, max_length=1000)),
                ('ios_msg', models.CharField(blank=True, max_length=1000)),
                ('ios_status', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
