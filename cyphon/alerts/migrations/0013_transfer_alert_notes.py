# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 17:46
from __future__ import unicode_literals

from django.db import migrations, transaction


def transfer_notes(apps, schema_editor):
    """Transfer existing relations between Alerts and Tags to TagRelations."""
    Alert = apps.get_model('alerts', 'Alert')
    Analysis = apps.get_model('alerts', 'Analysis')
    while Alert.objects.filter(notes__isnull=False).exists():
        with transaction.atomic():
            for alert in Alert.objects.filter(notes__isnull=False)[:1000]:
                Analysis.objects.create(
                    alert=alert,
                    notes=alert.notes
                )
                alert.notes = None
                alert.save()


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('alerts', '0012_auto_20170828_1343'),
    ]

    operations = [
        migrations.RunPython(
            transfer_notes,
            reverse_code=migrations.RunPython.noop
        ),
    ]
