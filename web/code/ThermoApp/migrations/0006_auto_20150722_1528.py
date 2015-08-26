# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0005_auto_20150722_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecastdata',
            name='fc_datetime',
            field=models.DateTimeField(verbose_name='Date Time', default=datetime.datetime(2015, 7, 22, 20, 28, 36, 78288, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 20, 28, 36, 1056, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 20, 28, 36, 23495, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 20, 28, 36, 22484, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 7, 22, 15, 28, 36, 29884)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_datetime',
            field=models.DateTimeField(verbose_name='Date Time', default=datetime.datetime(2015, 7, 22, 20, 28, 36, 52000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(verbose_name='Up Time', default=datetime.datetime(2015, 7, 22, 15, 28, 36, 56988)),
            preserve_default=True,
        ),
    ]
