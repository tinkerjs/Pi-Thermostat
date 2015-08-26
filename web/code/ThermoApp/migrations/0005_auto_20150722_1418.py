# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0004_auto_20150722_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forecastdata',
            old_name='rt_4dforecast',
            new_name='fc_4dforecast',
        ),
        migrations.RenameField(
            model_name='forecastdata',
            old_name='rt_outsidehumidity',
            new_name='fc_outsidehumidity',
        ),
        migrations.RenameField(
            model_name='forecastdata',
            old_name='rt_outsidetemp',
            new_name='fc_outsidetemp',
        ),
        migrations.RenameField(
            model_name='forecastdata',
            old_name='rt_plannerforecast',
            new_name='fc_plannerforecast',
        ),
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 19, 18, 38, 79692, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 19, 18, 38, 102340, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 19, 18, 38, 101336, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 7, 22, 14, 18, 38, 108517)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 19, 18, 38, 130749, tzinfo=utc), verbose_name='Date Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 7, 22, 14, 18, 38, 135338), verbose_name='Up Time'),
            preserve_default=True,
        ),
    ]
