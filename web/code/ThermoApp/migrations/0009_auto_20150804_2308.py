# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0008_auto_20150804_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicdata',
            name='hs_runtime',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(verbose_name='Up Time', default=datetime.datetime(2015, 8, 4, 23, 8, 53, 563276)),
            preserve_default=True,
        ),
    ]
