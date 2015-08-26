
# coding: utf-8

# # Thermostat Hardware Module
# 
# ## Description
# - The purpose of this application is to support a hardware interface used to provide real time sensor information to the overall application. This will be an automated application with no user interaction. This runs on a raspberry pi b+ using a 2.8" touch screen. 
# 
# ## Features
# - Control sensors
# - Read sensor data and provide to database
# - Read database data
# - Understand logic for controlling hardware
# 
# ## Issues
#  - TBD
# 
# ## The Code and methods
# - The following section contains the code that is used to make up the hardware interface. It is organized into sections that define configuration, modules that need to be imported and its own modules. 
# 
# ### Libraries to import

# In[1]:

import ThermoData #a module for accessing data
import RPi.GPIO as GPIO #import the RPI GPIO library 
import Adafruit_DHT # to read the temp from the AM2302
import time # to create delays and get time information
import os
import logging


# ### Configuration
# - Here we will setup the GPIO configuration for the Raspberry PI, define the pins and other hardware specific configuration tasks.

# In[2]:

#setup logging
logDir = os.path.join('/','thermostat','logs')
ThermoHardwareLogger = logging.getLogger('ThermoHardware')
fhandler = logging.FileHandler(filename=os.path.join(logDir,'thermohardware.log'), mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
ThermoHardwareLogger.addHandler(fhandler)
ThermoHardwareLogger.setLevel(logging.INFO)

ThermoHardwareLogger.info('100: Thermostat Hardware is starting')

dht_sensor = Adafruit_DHT.AM2302 #deinfe the type of DHT sensor for the adafruit lib

#assign pins to names
#BCM
dht_pin = 12
fan_pin = 21
heat_pin = 16
cool_pin = 20


#configure the GPIO pins
GPIO.setmode(GPIO.BCM) #set the mode of the GPIO 
GPIO.setup(fan_pin ,GPIO.OUT)
GPIO.setup(heat_pin, GPIO.OUT)
GPIO.setup(cool_pin, GPIO.OUT)

coolingHwStatus = ''
heatingHwStatus = ''
fanHwStatus = ''
offHwStatus = ''

ThermoHardwareLogger.info('101: Configuration complete')


# ### The hardware code

# In[3]:

def getHwInfo():
    try: 
        humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
        #logging.info('200: getHwInfo - H:{0} T:{1}'.format(round(humidity,2),round((temperature * 9/5 + 32),2)))
        return round(humidity,2), round((temperature * 9/5 + 32),2)
    except: 
        ThermoHardwareLogger.exception('Exception Occurred in ThermoHardware getHwInfo')
 
def writeTempHumid(hwTemp,hwHumidity):
    try:
        rtwQuery = ThermoData.getRealtimeData()
        rtwQuery.rt_currenttemp = hwTemp
        #print(hwTemp)
        rtwQuery.rt_humidity = hwHumidity
        
        #print(hwHumidity)
        #logging.info('300: writeTempHumid - T:{0} H{1}'.format(hwTemp,hwHumidity))
        ThermoData.updateRealTimeData(rtwQuery)
        #logging.info('300: writeTempHumid - db updated - H:{0} T{1}'.format(hwHumidity,hwTemp))
    except:
        ThermoHardwareLogger.exception('Exception Occurred in ThermoHardware writeTempHumid')
    
def getDBInfo():
    try: 
        rtrQuery = ThermoData.getRealtimeData()
        dbFanMode = rtrQuery.rt_fanmode
        dbDesTemp = rtrQuery.rt_destemp
        return dbFanMode,dbDesTemp
    except:
        ThermoHardwareLogger.exception('Exception Occurred in ThermoHardware getDBInfo')
                                                           
def controlHVAC(desiredTemp,hwTemp,fanMode='O'):
    global coolingHwStatus 
    global heatingHwStatus
    global fanHwStatus
    global offHwStatus
    
    
    #print('coolingHwStatus: ', coolingHwStatus)
    #print('heatingHwStatus: ', heatingHwStatus)
    #print('fanHwStatus: ', fanHwStatus)
    #print('offHwStatus: ', offHwStatus)
    
    try:
        if fanMode =='H': #heating
            fanHwStatus = 'Off'
            offHwStatus = 'Off'
            #turn off the other pins incase they were already on
            GPIO.output(cool_pin ,0)
            GPIO.output(fan_pin ,0)
            
            #compare the temp and either keep running or turn off 
            if desiredTemp > hwTemp:
                if heatingHwStatus != 'On':
                    ThermoData.updateHwEvent('Heating Started')
                    #print('Heating Started Event')
                    
                #ThermoData.updateHwEvent('Heating Started')
                GPIO.output(heat_pin ,1)
                heatingHwStatus = 'On'
            if desiredTemp + 1 < hwTemp:
                if heatingHwStatus != 'Off':
                    ThermoData.updateHwEvent('Heating Stopped')
                    #print('Heating stopped Event')
                heatingHwStatus = 'Off'
                GPIO.output(heat_pin ,0)

        if fanMode =='C': #cooling
            fanHwStatus = 'Off'
            offHwStatus = 'Off'
            #turn off the other pins incase they were already on
            GPIO.output(heat_pin ,0)
            GPIO.output(fan_pin ,0)
            
            #compare the temp and either keep running or turn off
            if desiredTemp < hwTemp:
                if coolingHwStatus != 'On':
                    ThermoData.updateHwEvent('Cooling Started')
                    #print('Cooling Started Event')
                
                GPIO.output(cool_pin ,1)
                coolingHwStatus = 'On'
            if desiredTemp - 1 > hwTemp:
                if coolingHwStatus != 'Off':
                    #print 'Cooling Off'
                    ThermoData.updateHwEvent('Cooling Stopped')
                coolingHwStatus = 'Off'
                #print('Cooling Stopped Event')
                GPIO.output(cool_pin ,0)

        if fanMode =='F': #Fan
            offHwStatus = 'Off'
            #turn off the other pins incase they were already on
            GPIO.output(cool_pin ,0)
            GPIO.output(fan_pin ,0)
            if fanHwStatus != 'On':
                    #print 'Cooling on'
                    ThermoData.updateHwEvent('Fan Started')
                    #print('Fan Started Event')
            #turn the fan on
            fanHwStatus = 'On'
            GPIO.output(fan_pin ,1)

        if fanMode =='A': #Auto
            pass

        if fanMode =='O': #Off
            fanHwStatus = 'Off'
            coolingHwStatus = 'Off'
            heatingHwStatus = 'Off'
            
            if offHwStatus != 'On':
                ThermoData.updateHwEvent('System Stopped')
                #print('System Off Event')
            offHwStatus = 'On'
            shutOffHVAC()
            
            
    except: 
        ThermoHardwareLogger.exception('Exception Occurred in ThermoHardware controlHVAC')
        
def shutOffHVAC():
    GPIO.output(heat_pin ,0)
    GPIO.output(cool_pin ,0)
    GPIO.output(fan_pin ,0)


# In[4]:

try:
    refreshCycle = 10
    while True: 
        hwHumidity, hwTemp = getHwInfo()
        fanMode, desTemp = getDBInfo()
        fanMode = str(fanMode)
        writeTempHumid(hwTemp,hwHumidity)
        #print(desTemp,hwTemp,fanMode)
        controlHVAC(desTemp,hwTemp,fanMode)
        
        #print 'Humidity:', hwHumidity
        #print 'Temp:', hwTemp
        #print 'Fan Mode:',fanMode.encode("ascii")
        #print 'Desired Temp:', desTemp
        
        time.sleep(refreshCycle) # delay for 10 sec to try and avoid db locks. May be able to handle this in the ThermoData module.

except:
    ThermoHardwareLogger.exception('Exception Occurred in ThermoHardware main loop')

finally:
    ThermoHardwareLogger.info('400: Cleanup GPIO')
    GPIO.cleanup()
    ThermoHardwareLogger.info('401: Thermostat Hardware is ending')


# ###Development

# In[ ]:

#rtQuery = ThermoData.getRealtimeData() 


# In[ ]:

#dir(rtQuery)
#rtQuery.rt_fanmode


# In[ ]:

#fanMode, desTemp = getDBInfo()
#print fanMode, desTemp


# In[ ]:

#GPIO.cleanup()


# In[ ]:

s = 'started'
'start' in s

