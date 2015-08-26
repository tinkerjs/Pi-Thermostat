# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ThermoApp', '0003_auto_20150624_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForecastData',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('rt_outsidetemp', models.IntegerField(verbose_name='Outside Temperature', default=0)),
                ('rt_outsidehumidity', models.IntegerField(verbose_name='Outside Humidity', default=0)),
                ('rt_4dforecast', models.TextField(verbose_name='Forecast Info')),
                ('rt_plannerforecast', models.TextField(verbose_name='Forecast Info')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='realtimedata',
            name='rt_forecast',
        ),
        migrations.RemoveField(
            model_name='realtimedata',
            name='rt_outsidehumidity',
        ),
        migrations.RemoveField(
            model_name='realtimedata',
            name='rt_outsidetemp',
        ),
        migrations.AlterField(
            model_name='automationdata',
            name='am_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 19, 10, 14, 433925, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_enddatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 19, 10, 14, 456787, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_startdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 19, 10, 14, 455569, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicdata',
            name='hs_uptime',
            field=models.TimeField(default=datetime.datetime(2015, 7, 22, 14, 10, 14, 463013)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_datetime',
            field=models.DateTimeField(verbose_name='Date Time', default=datetime.datetime(2015, 7, 22, 19, 10, 14, 485368, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='rt_uptime',
            field=models.TimeField(verbose_name='Up Time', default=datetime.datetime(2015, 7, 22, 14, 10, 14, 490431)),
            preserve_default=True,
        ),
    ]
