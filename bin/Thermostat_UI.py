
# coding: utf-8

# # Thermostat Interface
# 
# ## 1. Description
# The purpose of this application is to provide a user interface to control HVAC equipment also known as a thermostat. This runs on a raspberry pi b+ using a 2.8" touch screen. 
# 
# ## 2. Features
# 
# 
# ## 3. The Build
# The Pi needs to be configured to launch the python app at startup. Lets assume that our python app is called thermo.py. In order to do this: 
#     - create a file named /etc/xdg/autostart/thermo.desktop
#     - put the following contents into it
#         [Desktop Entry]
#         Type=Application
#         Name=LXPolKit
#         Exec=/home/pi/dev/thermostat/startthermo
#     - create a file named /home/pi/dev/thermostat/startthermo
#     - put the following contents into it
#         #!/bin/sh
#         sudo python /home/pi/dev/thermostat/thermo_tk.py
# Install python and the supporting libraires:
#     - sudo apt-get install python
#     - sudo apt-get intall pip
#     - sudo apt-get install python-tk
#     - DHT22
#         - sudo apt-get install build-essential python-dev
#         - git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#         - cd Adafruit_Python_DHT
#         - sudo python setup.py install
#     - pip install PIL
# Configure TFT Screen Rotation:
#     - nano /etc/modprobe.d/adafruit.conf
# Auto Calibrate Touch Screen
#      - /home/pi/Software/pit_tft_touch_cal.py 
#      
# 
# 
#         
# ## 4. Connections
# The GPIO header pins should be connected as follows:
# - pin 16 conected to Fan relay
# - pin 20 connected to Cooling relay
# - pin 21 connected to Heat relay
#     

# In[10]:

#Import the Rpi GPIO, UI and Image Graphics (PILLOW) libraries

from Tkinter import * #import the tkinter GUI library
import ttk #import the tkinter GUI library
from PIL import Image, ImageTk
import RPi.GPIO as GPIO #import the RPI GPIO library 
import time #import the time module
import Adafruit_DHT # to read the temp from the AM2302

import logging
import time
import os

logger = logging.getLogger()
fhandler = logging.FileHandler(filename=os.path.join('thermostat.log'), mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

logging.info('100: ***************Thermostat is starting************')

windowHeight = 240
windowWidth = 320

####- The main elements (root window, title and frames)
rootWindow = Tk()
rootWindow.resizable(0,0)
rootWindow.maxsize(width=windowWidth, height=windowHeight)
rootWindow.minsize(width=windowWidth, height=windowHeight)
rootWindow.title('Crib Connected Thermostat')
rootWindow.config(cursor="none")
rootWindow.resizable(0,0)
rootWindow.overrideredirect(1)
#rootWindow.columnconfigure(0, weight=1)
#rootWindow.columnconfigure(1, weight=1)
#rootWindow.columnconfigure(2, weight=1)
#rootWindow.columnconfigure(3, weight=1)
#rootWindow.rowconfigure(0, weight=1)
#rootWindow.rowconfigure(1, weight=1)
#rootWindow.rowconfigure(2, weight=1)
#rootWindow.rowconfigure(3, weight=1)



contentFrame = ttk.Frame(rootWindow, padding=(1,1,1,1))
contentFrame.config(cursor="none") 
contentFrame.columnconfigure(0, weight=1)
contentFrame.columnconfigure(1, weight=1)
contentFrame.columnconfigure(2, weight=1)
#contentFrame.columnconfigure(3, weight=1)
#contentFrame.columnconfigure(4, weight=1)
#contentFrame.columnconfigure(5, weight=1)
#contentFrame.columnconfigure(6, weight=1)
contentFrame.rowconfigure(0, weight=1)
contentFrame.rowconfigure(1, weight=1)
contentFrame.rowconfigure(2, weight=1)
#contentFrame.rowconfigure(3, weight=1)

manualFrame = ttk.Frame(rootWindow, padding=(1,1,1,1))
manualFrame.config(cursor="none") 
#manualFrame = ttk.Frame(rootWindow, borderwidth=5, relief='raised',width=400,height=200)
#mainFrame = ttk.Frame(content, borderwidth=1,width=400,height=200)
#mainFrame = ttk.Frame(rootWindow,padding='20 20 20 20')
#subFrame = ttk.Frame(rootWindow,padding='20 20 20 20').grid(column=1, row=0, sticky=(N, W, E, S))

####- Define some default values

desTempVal = IntVar() # a varibale to hold the desired temperature
fanMode = StringVar() # a variable to hold the fan mode. this can be used in place of 
                   # constantly updating the pin modes based on temperature. 

def set_desired_temp(value):
    logging.info('300: Desired temp set to {}'.format(value))
    #desired temperature
    #desTemp = 70;
    desTempVal.set(value)
    #print(desTempVal.get())
    #return desTempVal

def set_values():
    ####- Set and assign types to default values
    #current temperature
    logging.info('400: Setting some values')
    currTempVal = StringVar()
    currTempVal.set(temperature)

    #desired temperature
    #desTempVal = StringVar()
    #desTempVal.set(desTemp)

    #current humidity
    HumidityVal = StringVar()
    HumidityVal.set(humidity)
    
    airSelectionVal  = IntVar()
    
    return currTempVal, HumidityVal, airSelectionVal

# init hardware
def setup_dht_sensor():
    logging.info('500: Intialize temp humid sensor')
    dht_sensor = Adafruit_DHT.AM2302
    return dht_sensor

def get_temp_humid():
    try: 
        logging.info('600: Obtaining temp and humidity sensor values')
        humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
        temperature = round((temperature * 9/5 + 32),2)
        humidity = int(humidity)
        logging.debug('501: Temp is: {0} humidity is {1}'.format(temperature,humidity))
        return humidity, temperature
    except:
        return 1,1
    
def setup_gpio():
    logging.info('700: Setup GPIO')
    ##7. The GPIO and logic definition
    #assign pins to names
    #BCM
    dht_pin = 12
    fan_pin = 21
    heat_pin = 20
    cool_pin = 16
    
    #BOARD
    #dht_pin = 32
    #fan_pin = 40
    #heat_pin = 38
    #cool_pin = 36
    
    #configure the GPIO pins
    GPIO.setmode(GPIO.BCM) #set the mode of the GPIO 
    GPIO.setup(fan_pin ,GPIO.OUT)
    GPIO.setup(heat_pin, GPIO.OUT)
    GPIO.setup(cool_pin, GPIO.OUT)
    
    return dht_pin, fan_pin, heat_pin, cool_pin


dht_pin, fan_pin, heat_pin, cool_pin = setup_gpio()
dht_sensor = setup_dht_sensor()
humidity, temperature = get_temp_humid()
currTempVal, HumidityVal, airSelectionVal = set_values()
#desTempVal = set_desired_temp()

#Control Functions
def update_temphumid_values(humidity,temperature):
    logging.debug('800: Update temperature and humidity values')
    #current temperature
    currTempVal.set(temperature)
    #current humidity
    HumidityVal.set(humidity)
    logging.debug('801: Updated temperature {0} and humidity {1}'.format(temperature, humidity))

def updateTemp():
    logging.debug('900: Update temperature and humidity')
    humidity, temperature = get_temp_humid()
    update_temphumid_values(humidity,temperature)
    logging.debug('901: Updating temperature to {0} and humidity to {1}'.format(temperature, humidity))
    rootWindow.after(10000,updateTemp)
    

def turn_on_fan():
    logging.debug('1000: Turn on fan')
    GPIO.output(fan_pin ,1)
def turn_off_fan():
    GPIO.output(fan_pin ,0)
    logging.debug('1001: Turn off fan')

def turn_on_cool():
    logging.debug('1100: Turn on cooling')
    GPIO.output(cool_pin ,1)
def turn_off_cool():
    logging.debug('1101: Turn off cooling')
    GPIO.output(cool_pin ,0)
    
def turn_on_heat():
    logging.debug('1200: Turn on heating')
    GPIO.output(heat_pin ,1)
def turn_off_heat():
    logging.debug('1201: Turn off heating')
    GPIO.output(heat_pin ,0)
    
def raise_temp():
    logging.debug('1300: Raise desired temperature')
    tempval = desTempVal.get()
    newdesTemp = tempval  + 1
    set_desired_temp(newdesTemp)
    logging.debug('1301: Desired temperature set to {}'.format(newdesTemp))
    
def lower_temp():
    logging.debug('1400: Lower desired temperature')
    tempval = desTempVal.get()
    newdesTemp = tempval - 1
    set_desired_temp(newdesTemp)
    logging.debug('1401: Desired temperature set to {}'.format(newdesTemp))
    
def turn_off_everything():
    #turn everything off
    logging.debug('1500: Turn everything off')
    turn_off_fan()
    turn_off_cool()
    turn_off_heat()


def set_default_temp():
    logging.debug('1600: Set default temp')
    set_desired_temp(79)
    
def check_temperature(): #this is being called every 5 seconds. 
    logging.debug('1700: Checking the temperature')
    # i dont like calling the turn on or off function every time.
    # I want to set it and check what it is. 
    des_temp_value = desTempVal.get()
    air = airSelectionVal.get()
    logging.debug('1701: Desired temperature {0} actual temperature: {1}'.format(des_temp_value,temperature))
    #print(air)

        
    if air == 1: # heat
        if des_temp_value > temperature: 
            turn_on_heat()
        else: 
            turn_off_heat()
            
    elif air == 2: # cool
        
        if des_temp_value < temperature:
            turn_on_cool()
        else: 
            turn_off_cool()
    
    elif air == 3: # fan
        turn_on_fan()
        
    elif air == 4: # off
       turn_off_everything()
    
    elif air == 5: # Auto
        #rootWindow.after(100, turn_off_everything)
        if des_temp_value < temperature - 1: #77 < 79 -1 = 78
            turn_on_cool()
            turn_off_heat()
            turn_off_fan()
        elif des_temp_value > temperature + 1: # 77 > 74+1 = 75
            turn_on_heat()
            turn_off_cool()
            turn_off_fan()
        else: 
            turn_off_heat()
            turn_off_fan()
            turn_off_cool()
       
    rootWindow.after(5000,check_temperature)
    
def turnOnHVAC(mode):
    logging.debug('1800: Turning on HVAC mode: {}'.format(mode))

## Weather Functions

def get_weather_conditions():
    logging.debug('1900: Getting weather conditions')
    import urllib2
    import json
    f = urllib2.urlopen('http://api.wunderground.com/api/4d5dbde505034b47/geolookup/conditions/q/TX/Frisco.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    #print parsed_json
    precipitation = parsed_json['current_observation']['precip_today_string']
    #print'Precipitation {0}'.format(precipitation)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    #print "Current temperature in %s is: %s" % (location, temp_f)
    f.close()
    
def get_weather_planner():
    logging.debug('2000: Getting weather planner')
    import urllib2
    import json
    days='04260426' #set this to the days you want to plan between
    f = urllib2.urlopen('http://api.wunderground.com/api/4d5dbde505034b47/geolookup/planner_{0}/q/TX/Frisco.json'.format(days))
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    return parsed_json



#get_weather_conditions()
#planner = get_weather_planner()

## managment functions
def show_manualframe():
    logging.debug('2100: Show manual frame')
    contentFrame.lower()
    manualFrame.lift()
    
def hide_manualframe():
    logging.debug('2200: Hide manual frame')
    manualFrame.lower()
    contentFrame.lift()

def setMode():
    logging.debug('2300: Set mode')
    
def quitUi():
    logging.debug('2400: Quitting application')
    rootWindow.destroy()

rootWindow.after(5000,check_temperature)
rootWindow.after(10000,updateTemp)

rootWindow.after(1000,set_default_temp)

##labels
#current temperature
label_currTemp = ttk.Label(contentFrame, text='Current:')
label_currTempVal = ttk.Label(contentFrame, textvariable=currTempVal) #currTempVal used here!

#desired temperature
label_desTemp = ttk.Label(contentFrame, text='Desired:')
label_desTempVal = ttk.Label(contentFrame, textvariable=desTempVal) #desTepVal user here!


#humidity
label_Humidity = ttk.Label(contentFrame, text='Humidity:')
label_HumidityVal = ttk.Label(contentFrame, textvariable=HumidityVal) #HumidityVal used here!

#AirSelection
label_airSelection = ttk.Label(contentFrame, text='Air:')



##Buttons
btn_fan_on = ttk.Button(manualFrame, text='Fan On', command=turn_on_fan)
btn_fan_off = ttk.Button(manualFrame, text='Fan Off', command=turn_off_fan)
btn_cool_on = ttk.Button(manualFrame, text='Cooling On', command=turn_on_cool)
btn_cool_off = ttk.Button(manualFrame, text='Cooling Off', command=turn_off_cool)
btn_heat_on = ttk.Button(manualFrame, text='Heating On', command=turn_on_heat)
btn_heat_off = ttk.Button(manualFrame, text='Heating Off', command=turn_off_heat)

btn_raise_temp = ttk.Button(contentFrame, text='Raise', command=raise_temp)
btn_lower_temp = ttk.Button(contentFrame, text='Lower', command=lower_temp)


btn_contentQuit = ttk.Button(contentFrame, text='Exit', command=quitUi)
btn_showManualFrame = ttk.Button(contentFrame, text='Config', command=show_manualframe)
btn_hideManualFrame = ttk.Button(manualFrame, text='Control', command=hide_manualframe)

btn_manualQuit = ttk.Button(manualFrame, text='Exit', command=quitUi)

radio_airSelectionHeat= ttk.Radiobutton(contentFrame, text='Heat', variable=airSelectionVal, value=1, command = setMode)
radio_airSelectionCool= ttk.Radiobutton(contentFrame, text='Cool', variable=airSelectionVal, value=2,  command = setMode)
radio_airSelectionFan= ttk.Radiobutton(contentFrame, text='Fan', variable=airSelectionVal, value=3,  command = setMode)
radio_airSelectionOff= ttk.Radiobutton(manualFrame, text='Off', variable=airSelectionVal, value=4,  command = setMode)
radio_airSelectionAuto= ttk.Radiobutton(contentFrame, text='Auto', variable=airSelectionVal, value=5,  command = setMode)


####- Grid stuff

def grid_stuff():
    logging.debug('2500: Grid widgets')
    #main window and frames
    manualFrame.grid(column=0, row=0, sticky='nsew')
    contentFrame.grid(column=0, row=0, sticky='nsew')
    #mainFrame.grid(column=0, row=0,columnspan=5, rowspan=5, sticky=(N,S,E,W))

    #buttons
    #button configs
    btnpad_x = 1
    btnpad_y = 1
    btncolspan = 1
    btnrowspan = 1
    btnsticky = ()
    
    #Manual Frame
    btn_fan_on.grid(column=0, row=0, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    btn_fan_off.grid(column=1, row=0, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    
    btn_heat_on.grid(column=0, row=1, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    btn_heat_off.grid(column=1, row=1, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    
    btn_cool_on.grid(column=0, row=2, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    btn_cool_off.grid(column=1, row=2, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    
    btn_hideManualFrame.grid(column=2, row=0, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    btn_manualQuit.grid(column=2, row=1, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    
    radio_airSelectionOff.grid(column=0, row=7, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)

    #Content Frame
    btn_raise_temp.grid(column=2, row=0, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    btn_lower_temp.grid(column=2, row=1, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
   
    btn_showManualFrame.grid(column=2, row=2, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    #btn_contentQuit.grid(column=2, row=8, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
   
    radio_airSelectionHeat.grid(column=3, row=0, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    radio_airSelectionCool.grid(column=3, row=1, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    radio_airSelectionFan.grid(column=3, row=2, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    #This might damage the HVAC Unit. 
    #radio_airSelectionAuto.grid(column=0, row=7, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    
    #labels
    lblpad_x = 1
    lblpad_y = 1
    lblcolspan = 1
    lblrowspan = 1
    label_currTemp.grid(column=0, row = 0, columnspan=lblcolspan, rowspan=lblrowspan,sticky=(N,S), pady=lblpad_y, padx=lblpad_x)
    label_currTempVal.grid(column=1, row = 0, columnspan=lblcolspan, rowspan=lblrowspan,sticky=(N,S), pady=lblpad_y, padx=lblpad_x)
    label_desTemp.grid(column=0, row = 1, columnspan=lblcolspan, rowspan=lblrowspan,sticky=(N,S), pady=lblpad_y, padx=lblpad_x)
    label_desTempVal.grid(column=1, row = 1, columnspan=lblcolspan, rowspan=lblrowspan, sticky=(N,S), pady=lblpad_y, padx=lblpad_x)
    label_Humidity.grid(column=0, row = 2, columnspan=lblcolspan, rowspan=lblrowspan,sticky=(N,S), pady=lblpad_y, padx=lblpad_x)
    label_HumidityVal.grid(column=1, row = 2, columnspan=lblcolspan, rowspan=lblrowspan, sticky=(N,S), pady=lblpad_y, padx=lblpad_x)
    #label_airSelection.grid(column=0, row = 5, columnspan=lblcolspan, rowspan=lblrowspan, sticky=(N,S), pady=lblpad_y, padx=lblpad_x)


grid_stuff()

#Run the main loop
rootWindow.mainloop()

##8. Clean up the GPIO
GPIO.cleanup()


# In[5]:

#GPIO.cleanup()


# In[ ]:

#print forecast
#precipitation = planner['trip']['precip']['max']['in']
#print planner['trip']
#print precipitation
#print'24hr Preceipitation is {0} %'.format(float(precipitation)*100)
#location = parsed_json['location']['city']
#temp_f = parsed_json['current_observation']['temp_f']
#print "Current temperature in %s is: %s" % (location, temp_f)


# In[ ]:



