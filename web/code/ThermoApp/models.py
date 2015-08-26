from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
#steps to rebuild DB
    #1. delete DB file from disk
    #2. Remove migrations folder from app folder if any
    #3. python3 manage.py makemigrations ThermoApp
    #4. python3 manage.py migrate
    #5. python manage.py createsuperuser
    
#steps to update DB
    #Change your models (in models.py).
    #Run python3 manage.py makemigrations to create migrations for those changes
    #Run python3 manage.py migrate to apply those changes to the database

# data for automation information
class commonData(models.Model):
    date_time = models.DateTimeField(null=True)
    
    class Meta:
        abstract=True

class AutomationData(commonData):
    am_datetime = models.DateTimeField(null=True)
    am_dayofweek  =  models.CharField(max_length = 2)
    am_temp  = models.IntegerField(default = 0)
    am_fanmode  = models.CharField(max_length = 10)
    am_forecastdur = models.IntegerField(default = 0)
    
    #provides some support for looking at objects.all method
    def __str__(self):
        return str(self.am_datetime)

# data for historical reporting
class HistoricData(commonData):
	hs_eventid  = models.CharField(max_length = 10, default ='Default')
	hs_eventdesc = models.CharField(default='Default',max_length=50)
	hs_eventdatetime = models.DateTimeField(null=True)
	#data from RealtimeData
	hs_currenttemp = models.IntegerField(default=0)
	hs_destemp = models.IntegerField(default=0)
	hs_humidity = models.IntegerField(default=0)
	hs_fanmode = models.CharField(max_length = 10)
	hs_outsidetemp = models.IntegerField(default=0)
	hs_outsidehumidity = models.IntegerField(default=0)
	hs_forecast = models.TextField()
	hs_runtime = models.TimeField(null=True)
	hs_uptime = models.TimeField(null=True)
	#provides some support for looking at objects.all method
	def __str__(self):
		return str(self.hs_eventid )

# data for real time information
class RealtimeData(commonData): #this is inheriting form the commonData model 
	#the first value is the code reference name and the column_name in the DB. 'rt_temperature'
	rt_datetime = models.DateTimeField('Date Time', null=True)
	#rt_currenttemp = models.IntegerField('Current Tempterature', default=0)
	rt_currenttemp = models.DecimalField('Current Tempterature', max_digits=5, decimal_places=2, default=0)
	#rt_destemp = models.IntegerField('Desired Temperature', default=0)
	rt_destemp = models.DecimalField('Desired Temperature', max_digits=5, decimal_places=2, default=78)
	#rt_humidity = models.IntegerField('Humidity', default=0)
	rt_humidity = models.DecimalField('Humidity', max_digits=5, decimal_places=2, default=78)
	rt_fanmode_choices = (
						 ('H', 'Heat'), 
						 ('C', 'Cool'), 
						 ('F', 'Fan'), 
						 ('A', 'Auto'),
						 ('O', 'Off'),                                   
						 )
	rt_fanmode = models.CharField('Fan Mode', max_length = 10, choices=rt_fanmode_choices)
	rt_runtime = models.IntegerField('Run Time', default=0)
	rt_uptime = models.TimeField('Up Time', null=True)
	rt_hWstatus = models.CharField(max_length = 20, null=True)

	def __str__(self):
		return str(self.rt_currenttemp)

class ForecastData(commonData):
    fc_datetime = models.DateTimeField('Date Time', null=True)
    fc_outsidetemp = models.IntegerField('Outside Temperature', default=0)
    fc_outsidehumidity = models.IntegerField('Outside Humidity', default=0)
    fc_4dforecast = models.TextField('Forecast Info')
    fc_plannerforecast = models.TextField('Forecast Info')
    
    #provides some support for looking at objects.all method
    
    def __str__(self):
        return str(self.fc_datetime)