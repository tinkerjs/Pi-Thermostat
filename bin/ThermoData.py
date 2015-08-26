
# coding: utf-8

# # Thermostat Data Module
# 
# ## Description
# - The purpose of this notebook is to support a database interface to control HVAC equipment also known as a thermostat. This runs on a raspberry pi b+ using DJANGO.This will be the code that make up the database interface for the thermostat application. 
# 
# 
# ## The Build
# - The Pi needs to be configured to launch the python app at startup. Lets assume that our python app is called thermo.py. In order to do this: 
#     - create the file named /etc/xdg/autostart/startup.desktop
#     - put the following contents into it
#         [Desktop Entry]
#         Type=Application
#         Name=LXPolKit
#         Exec=/startup
#     - create the file /startup
#     - put the following contents into it
#     
# <code>#!/bin/bash
# sudo python /thermostat/bin/ThermoGui.py &
# sudo /thermostat/bin/djrunserver &
# sudo /thermostat/bin/ipythonnotebook & </code>
#         
#         
# - Install python and the supporting libraires:
#     - sudo apt-get install python
#     - sudo apt-get intall pip
#     - Python tk (already inlcuded in 2.7)
#         - sudo apt-get install python-tk
#     - Python image library
#         - pip install PIL
#     - Python Time Zone
#         - pip install pytz   
# - The pi does need the environment variable DJANGO_SETTINGS_MODULE set to = thermostat.settings for importing the settings when starting up. This is handled during the import section. 
# - The database uses the embedded sqlite db that comes with DJANGO.  
# - There is a cron job that is executed every hour that is divisible by 4 to retrieve the weather forcast using the ThermoData moule from a cmd line. 
#     - The job is added to the sudo cronttab by running <code>sudo crontab -e</code>
#     - the cron job is: 01 */4 * * * /thermostat/bin/getWeatherForecast
#     - The code for the getWeatherForeCast is
#     
# <code>#! /bin/bash
# cd /thermostat/bin/
# python ThermoData.py getWeatherForecast
# echo "getWeatherForcast script ran: $(date)" >> /thermostat/logs/forecast_cron.log</code>
# 
# - Wifi
#     - This PI uses an Airlink101 Wireless N USB adapter. To configure follow these steps:
#         - Confogire the adapter using the GUI config tool in the raspbian os.
#         - Add "scan_ssid=1" to the /etc/wpa_supplicant/wpa_supplicant.conf file in the "network" section
# 
# ## Features
# - Allow for methods to add, update and retrieve data.
# - Allow for querying data
# - Data retention and managment. 
# - log file cleanup
# - cmd line interface
# 
# ## Issues
# - In the hardware module ive put in a delay of 20 seconds to try and avoid running into scenarios where I can not write to the DB becuase it is locked. Need to handle this in the data module itself. 
# - When changing the fan mode from the UI it causes the desired temp to jump to an old value. 

# ## 5. The Code and methods
# - The following section contains the code that is used to make up the data interface. It is organized into sections that define configuration, modules that need to be imported and its own modules. 
# 
# ### Libraries to import

# In[ ]:

import os 
import sys
import logging
import django
from django.utils import timezone as djTimeZone
from pytz import timezone as pytzTimeZone 
import datetime

sys.path.append('/thermostat/web/code/') #so we can import django modules  


#these are the models that are defined for the database
os.chdir('/thermostat/web/code/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thermostat.settings') ##this one is so critical. Use this rather than exporting it from the shell
django.setup()

from ThermoApp.models import RealtimeData as RTdata
from ThermoApp.models import ForecastData as FCdata
from ThermoApp.models import HistoricData as HSdata


# ### Configuration
# -  DJANGO needs to be setup in order to be able to use the applications files. It needs to be called from inside the app directory where manage.py lives '/thermostat/web/code/'.

# In[ ]:

#setup logging
logDir = os.path.join('/','thermostat','logs')
thermoDataLogger = logging.getLogger('ThermoData')
fhandler = logging.FileHandler(filename=os.path.join(logDir,'thermodata.log'), mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
thermoDataLogger.addHandler(fhandler)
thermoDataLogger.setLevel(logging.INFO)

thermoDataLogger.info('100: Thermostat Data is starting')

central = pytzTimeZone('US/Central')

thermoDataLogger.info('101: Configuration is complete')


# ### Work with  Data
# - So far these methods dont really do anything beyond the DJANGO native model API. At some point these will be customized to offer validation and error handling for the application specific needs.
# 
# ####Get real time data
# - this will only return the first and assumedly only record in the real time table.  

# In[ ]:

def getRealtimeData():
    try: 
        dataQuery = RTdata.objects.get(pk=1)
        return dataQuery
    except:
        thermoDataLogger.exception('Exception Occurred in ThermoData getRealtimeData()')


# #### Update real time data
# - This will take whatever data i have updated and save it to the db. It will also update the rt_date time each time it is called to keep the time up to date in the DB. 

# In[ ]:

def updateRealTimeData(queryset):
    try: 
        queryset.rt_datetime = djTimeZone.now()
        queryset.save()
    except:
        thermoDataLogger.exception('Exception Occurred in ThermoData updateRealtimeData().')


# ####Get Forecast Data
# - this will retreive all the records from the forecast data table.  

# In[ ]:

def getForecastData():
    try: 
        forecastQuery = FCdata.objects.get(pk=1)
        return forecastQuery
    except:
        thermoDataLogger.exception('Exception Occurred in ThermoData getForecastData()')


# ####Update Forecast Data
# - this will update all the records from the forecast data table.  

# In[ ]:

def updateForecastData(queryset):
    try: 
        queryset.fc_datetime = djTimeZone.now()
        queryset.save()
    except:
        thermoDataLogger.exception('Exception Occurred in ThermoData updateForecastData().')


# ####Get the weather forceast and information
# This will be used to make webservice calls to weather underground to get weather data and store in the database to be used  throughout the application. 

# In[ ]:

def getWeatherForecast():
    #get the current conditions
    apiId = '4d5dbde505034b47'
    state= 'TX'
    city = 'Frisco'
    import urllib2
    import json
    currCondFile = urllib2.urlopen('http://api.wunderground.com/api/{2}/geolookup/conditions/q/{0}/{1}.json'.format(state,city,apiId))
    currCondJson = currCondFile.read()
    parsedCurrCondJson = json.loads(currCondJson)
    
    #current conditions by element
    currPrecipitation = parsedCurrCondJson['current_observation']['precip_today_string']
    currLocation = parsedCurrCondJson['location']['city']
    currTemp_f = parsedCurrCondJson['current_observation']['temp_f']
    currRealtiveHumidity = parsedCurrCondJson['current_observation']['relative_humidity']
    currCondFile.close()
        
    #Get todays forecast
    tdForecastFile = urllib2.urlopen('http://api.wunderground.com/api/4d5dbde505034b47/forecast/q/TX/Frisco.json')
    tdForecastJson = tdForecastFile.read()
    tdForecastJsonParsed = json.loads(tdForecastJson)
    #uses simple forecast call to get data for the next 4 days
    fcList = []
    for day in tdForecastJsonParsed['forecast']['simpleforecast']['forecastday']:
        fcConditions = day['conditions']
        fcDay = day['date']['weekday_short']
        fcDayHigh = day['high']['fahrenheit']
        fcDayLow = day['low']['fahrenheit']
        fcList.append(fcDay.encode('ascii') + ' ' + fcDayHigh.encode('ascii') +'/'+ fcDayLow.encode('ascii') + ' ' + fcConditions.encode('ascii'))
    
    #print '\n'.join(fcList)
    
    tdForecastFile.close()
    
    fcQuery = getForecastData()
    fcQuery.fc_outsidetemp = currTemp_f
    fcQuery.fc_outsidehumidity = currRealtiveHumidity.strip('%')
    fcQuery.fc_4dforecast = '{0}'.format('\n'.join(fcList))
    updateForecastData(fcQuery)
   
    return parsedCurrCondJson
    
#tdForecastJsonParsed = getWeatherForecast()


# ####Update events to the DB 
# - this will create a hardware event entry and update the end time of the event when it has completed. Event descriptions can be:
#     - coolingStart, coolingStop - when the cooling system is turned on/off
#     - heatingStart, heatingStop - when the heating system is turned on/off
#     - fanStart, fanStop - when the fan is turned on/off

# In[ ]:

def updateHwEvent(eventDesc):
    if 'Start' in eventDesc:
        #print 'event start: %s' %eventDesc
        hsRtQuery = getRealtimeData()
        hsFcQuery = getForecastData()
        eventStartTime = djTimeZone.now()
        startEventDB = HSdata(hs_eventdesc = eventDesc,
                              hs_eventdatetime = eventStartTime, 
                              hs_currenttemp = hsRtQuery.rt_currenttemp, 
                              hs_destemp = hsRtQuery.rt_destemp, 
                              hs_humidity = hsRtQuery.rt_humidity, 
                              hs_fanmode = hsRtQuery.rt_fanmode, 
                              hs_outsidetemp = hsFcQuery.fc_outsidetemp, 
                              hs_outsidehumidity = hsFcQuery.fc_outsidehumidity, 
                              hs_forecast = hsFcQuery.fc_4dforecast)
        startEventDB.save()
    if 'Stop' in eventDesc:
        #print 'event stop: %s' %eventDesc
        hsRtQuery = getRealtimeData()
        hsFcQuery = getForecastData()
        eventStopTime = djTimeZone.now()
        stopEventDB = HSdata(hs_eventdesc = eventDesc,
                              hs_eventdatetime = eventStopTime, 
                              hs_currenttemp = hsRtQuery.rt_currenttemp, 
                              hs_destemp = hsRtQuery.rt_destemp, 
                              hs_humidity = hsRtQuery.rt_humidity, 
                              hs_fanmode = hsRtQuery.rt_fanmode, 
                              hs_outsidetemp = hsFcQuery.fc_outsidetemp, 
                              hs_outsidehumidity = hsFcQuery.fc_outsidehumidity, 
                              hs_forecast = hsFcQuery.fc_4dforecast)
        stopEventDB.save()


# In[ ]:

#updateHwEvent('Fan Start')


# In[ ]:




# #### Command line application suppot and CRON
# This section will provide supporting code to allow the data module to be executed as a scipt for timed jobs by CRON or executed independently  

# In[ ]:

if __name__ == '__main__':
    args = sys.argv[1:]
    if 'getWeatherForecast' in args:
        print 'Getting weather forecast'
        getWeatherForecast()
    else:
        print '''
        ThermoData cmd line interface can be called with 
        the following options using sudo:
        - sudo python ThermoData.py getWeatherForecast - to get the 
          latest forecast data from weather underground. 
        - more to come...
        '''


# ###Development and Testing

# In[ ]:

#rtQuery = getRealtimeData()
#print(rtQuery.rt_currenttemp)


# In[ ]:

#rtQuery.rt_currenttemp = 27.50


# In[ ]:

#updateRealTimeData(rtQuery)


# In[ ]:

#timezone.now()

