# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0002_realtimedata_rt_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledata',
            name='sd_weekday',
            field=models.CharField(default='Su', max_length=2),
            preserve_default=True,
        ),
    ]
