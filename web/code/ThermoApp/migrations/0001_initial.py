# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomationData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('am_datetime', models.DateTimeField(default=datetime.datetime(2015, 6, 11, 3, 58, 26, 565198, tzinfo=utc))),
                ('am_dayofweek', models.CharField(default='Su', max_length=2)),
                ('am_temp', models.IntegerField(default=0)),
                ('am_fanmode', models.CharField(default='Default', max_length=10)),
                ('am_forecastdur', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('hs_eventid', models.CharField(default='Default', max_length=10)),
                ('hs_startdatetime', models.DateTimeField(default=datetime.datetime(2015, 6, 11, 3, 58, 26, 588024, tzinfo=utc))),
                ('hs_enddatetime', models.DateTimeField(default=datetime.datetime(2015, 6, 11, 3, 58, 26, 589224, tzinfo=utc))),
                ('hs_currenttemp', models.IntegerField(default=0)),
                ('hs_destemp', models.IntegerField(default=0)),
                ('hs_humidity', models.IntegerField(default=0)),
                ('hs_fanmode', models.CharField(default='Default', max_length=10)),
                ('hs_outsidetemp', models.IntegerField(default=0)),
                ('hs_outsidehumidity', models.IntegerField(default=0)),
                ('hs_forecast', models.TextField(default='Default')),
                ('hs_runtime', models.IntegerField(default=0)),
                ('hs_uptime', models.TimeField(default=datetime.datetime(2015, 6, 10, 22, 58, 26, 595509))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RealtimeData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_time', models.DateTimeField(null=True)),
                ('rt_datetime', models.DateTimeField(default=datetime.datetime(2015, 6, 11, 3, 58, 26, 617587, tzinfo=utc), verbose_name='Date Time')),
                ('rt_currenttemp', models.IntegerField(default=0, verbose_name='Current Tempterature')),
                ('rt_destemp', models.IntegerField(default=0, verbose_name='Desired Temperature')),
                ('rt_humidity', models.IntegerField(default=0, verbose_name='Humidity')),
                ('rt_fanmode', models.CharField(verbose_name='Fan Mode', max_length=10, choices=[('H', 'Heat'), ('C', 'Cool'), ('F', 'Fan'), ('A', 'Auto'), ('O', 'Off')])),
                ('rt_outsidetemp', models.IntegerField(default=0, verbose_name='Outside Temperature')),
                ('rt_outsidehumidity', models.IntegerField(default=0, verbose_name='Outside Humidity')),
                ('rt_forecast', models.TextField(verbose_name='Forecast Info')),
                ('rt_runtime', models.IntegerField(default=0, verbose_name='Run Time')),
                ('rt_uptime', models.TimeField(default=datetime.datetime(2015, 6, 10, 22, 58, 26, 623783), verbose_name='Up Time')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
