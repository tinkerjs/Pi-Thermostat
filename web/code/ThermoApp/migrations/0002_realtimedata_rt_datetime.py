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
        migrations.AddField(
            model_name='realtimedata',
            name='rt_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 5, 20, 0, 336149, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
