# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 17, 44, 22, 859985, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='automationdata',
            name='am_fanmode',
            field=models.CharField(default='Off', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 17, 44, 22, 883893, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 17, 44, 22, 882855, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
