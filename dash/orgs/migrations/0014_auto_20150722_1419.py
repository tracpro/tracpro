# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0013_auto_20150715_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='domain',
            field=models.CharField(null=True, error_messages={b'unique': 'This domain is not available'}, max_length=255, blank=True, help_text='The custom domain for this organization', unique=True, verbose_name='Domain'),
        ),
        migrations.AlterField(
            model_name='org',
            name='subdomain',
            field=models.SlugField(null=True, error_messages={b'unique': 'This subdomain is not available'}, max_length=255, blank=True, help_text='The subdomain for this organization', unique=True, verbose_name='Subdomain'),
        ),
        migrations.AlterField(
            model_name='org',
            name='timezone',
            field=models.CharField(default='UTC', help_text='The timezone your organization is in.', max_length=64, verbose_name='Timezone'),
        ),
    ]
