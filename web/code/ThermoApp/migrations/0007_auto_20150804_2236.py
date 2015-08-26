# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0006_auto_20150722_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='automationdata',
            name='date_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historicdata',
            name='date_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historicdata',
            name='hs_eventdesc',
            field=models.CharField(default='Default', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 5, 3, 35, 58, 862300, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forecastdata',
            name='fc_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 5, 3, 35, 58, 949822, tzinfo=utc), verbose_name='Date Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 5, 3, 35, 58, 890860, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 5, 3, 35, 58, 889686, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 8, 4, 22, 35, 58, 897088)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 5, 3, 35, 58, 923228, tzinfo=utc), verbose_name='Date Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 8, 4, 22, 35, 58, 928052), verbose_name='Up Time'),
            preserve_default=True,
        ),
    ]
