# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0009_auto_20150804_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(verbose_name='Up Time', null=True),
            preserve_default=True,
        ),
    ]
