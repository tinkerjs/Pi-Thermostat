# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0010_auto_20150804_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicdata',
            old_name='hs_enddatetime',
            new_name='hs_eventdatetime',
        ),
        migrations.RemoveField(
            model_name='historicdata',
            name='hs_startdatetime',
        ),
    ]
