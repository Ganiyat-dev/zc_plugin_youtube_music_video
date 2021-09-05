# Generated by Django 3.2.4 on 2021-09-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('artiste', models.CharField(max_length=100, verbose_name='artiste')),
                ('album', models.CharField(max_length=100, verbose_name='album')),
                ('media_thumbnail', models.URLField()),
                ('media_url', models.URLField()),
                ('likes', models.IntegerField(default=0)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('time_added',),
            },
        ),
    ]
