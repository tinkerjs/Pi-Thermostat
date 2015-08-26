# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0002_auto_20150624_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 4, 25, 9, 507970, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 4, 25, 9, 531952, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 4, 25, 9, 530872, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 6, 24, 23, 25, 9, 538563)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_datetime',
            field=models.DateTimeField(verbose_name='Date Time', default=datetime.datetime(2015, 6, 25, 4, 25, 9, 561705, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_humidity',
            field=models.DecimalField(verbose_name='Humidity', max_digits=5, default=78, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(verbose_name='Up Time', default=datetime.datetime(2015, 6, 24, 23, 25, 9, 568692)),
            preserve_default=True,
        ),
    ]
