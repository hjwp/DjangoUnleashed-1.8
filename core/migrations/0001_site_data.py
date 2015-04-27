# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def add_site_data(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    new_domain = 'getorganized.com'
    new_name = 'Get Organized!'
    if Site.objects.exists():
        current_site = Site.objects.get(pk=1)
        current_site.domain = new_domain
        current_site.name = new_name
        current_site.save()
    else:
        current_site = Site(
            pk=1,  # coerce primary key
            domain=new_domain,
            name=new_name)
        current_site.save()


def remove_site_data(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    current_site = Site.objects.get(pk=1)
    current_site.domain = 'example.com'
    current_site.name = 'example.com'
    current_site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_site_data,
            remove_site_data,
        ),
    ]
