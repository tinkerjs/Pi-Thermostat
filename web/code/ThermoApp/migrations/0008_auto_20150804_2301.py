# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0007_auto_20150804_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='automationdata',
            name='am_dayofweek',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='automationdata',
            name='am_fanmode',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forecastdata',
            name='fc_datetime',
            field=models.DateTimeField(null=True, verbose_name='Date Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_fanmode',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_forecast',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_runtime',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_uptime',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_datetime',
            field=models.DateTimeField(null=True, verbose_name='Date Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 8, 4, 23, 1, 14, 321304), verbose_name='Up Time'),
            preserve_default=True,
        ),
    ]
