# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0002_action_project'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='action',
            unique_together=set([('url', 'project')]),
        ),
    ]