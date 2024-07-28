# Generated by Django 5.0.6 on 2024-07-28 11:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='connection',
            name='from_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections_sent', to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='connection',
            name='to_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections_received', to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='profileview',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_views', to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='profileview',
            name='viewed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_profiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skill',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_from_profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
