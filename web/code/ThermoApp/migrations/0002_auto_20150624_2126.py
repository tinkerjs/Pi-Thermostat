# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 2, 26, 27, 224791, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 2, 26, 27, 247249, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 2, 26, 27, 246226, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 6, 24, 21, 26, 27, 253185)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_currenttemp',
            field=models.DecimalField(max_digits=5, verbose_name='Current Tempterature', default=0, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_datetime',
            field=models.DateTimeField(verbose_name='Date Time', default=datetime.datetime(2015, 6, 25, 2, 26, 27, 274768, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_destemp',
            field=models.DecimalField(max_digits=5, verbose_name='Desired Temperature', default=78, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_humidity',
            field=models.DecimalField(max_digits=5, verbose_name='Humidity', default=0, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(verbose_name='Up Time', default=datetime.datetime(2015, 6, 24, 21, 26, 27, 281129)),
            preserve_default=True,
        ),
    ]
