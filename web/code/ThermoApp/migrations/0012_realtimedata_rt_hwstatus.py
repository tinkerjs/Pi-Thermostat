# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0011_auto_20150804_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtimedata',
            name='rt_hWstatus',
            field=models.CharField(null=True, max_length=10),
            preserve_default=True,
        ),
    ]
