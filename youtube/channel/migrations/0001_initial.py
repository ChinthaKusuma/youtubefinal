# Generated by Django 5.1.5 on 2025-02-06 18:42

import channel.models
import django.db.models.deletion
import taggit.managers
import videos.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_art', models.ImageField(blank=True, default='channel-art.jpg', null=True, upload_to=videos.models.user_directory_path)),
                ('image', models.ImageField(blank=True, null=True, upload_to=videos.models.user_directory_path)),
                ('full_name', models.CharField(max_length=200)),
                ('channel_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('disable', 'Disable')], default='active', max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('total_views', models.IntegerField(default=0)),
                ('business_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('make_business_email_public', models.BooleanField(default=False)),
                ('business_location', models.CharField(blank=True, max_length=500, null=True)),
                ('make_business_location_public', models.BooleanField(default=False)),
                ('website', models.URLField(default='https://my-website.com/')),
                ('instagram', models.URLField(default='https://isntagram.com/')),
                ('facebook', models.URLField(default='https://facebook.com/')),
                ('twitter', models.URLField(default='https://twitter.com/')),
                ('keywords', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('subscribers', models.ManyToManyField(related_name='user_subs', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=channel.models.user_directory_path)),
                ('content', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('disable', 'Disable')], default='active', max_length=100)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.channel')),
                ('likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Community',
                'verbose_name_plural': 'Community Posts',
            },
        ),
        migrations.CreateModel(
            name='CommunityComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=10000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='channel.community')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Community Comments',
                'verbose_name_plural': 'Community Comments',
            },
        ),
    ]
