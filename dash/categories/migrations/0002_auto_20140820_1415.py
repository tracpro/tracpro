# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def pollcategory_to_category(apps, schema_editor):
    pass  # maintain for backwards compatibility


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(pollcategory_to_category),
    ]
