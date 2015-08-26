# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0002_auto_20150519_0027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtimedata',
            old_name='rt_forccast',
            new_name='rt_forecast',
        ),
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 5, 28, 51, 165035, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 5, 28, 51, 187262, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 5, 28, 51, 186250, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 5, 19, 0, 28, 51, 193275)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 5, 19, 0, 28, 51, 220125)),
            preserve_default=True,
        ),
    ]
