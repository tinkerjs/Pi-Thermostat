
# coding: utf-8

# # Thermostat GUI Module
# 
# ## Description
# - The purpose of this application is to support a graphical user interface used to provide an easy to use interface for manipulating the thermostat application. This runs on a raspberry pi b+ using a 2.8" touch screen. 
# 
# ## Features
# - Display values
# - Accept user inputs
# - Take actions based on inputs, such as calling the data interface or updating the display. 
# 
# ## The build
# - Install python and the supporting libraires:
# 
# 
# ## Issues
# - TBD
# 
# ## The Code and methods
# - The following section contains the code that is used to make up the data interface. It is organized into sections that define configuration, modules that need to be imported and its own modules. 
# 
# ### Libraries to import

# In[1]:

from Tkinter import * #import the tkinter GUI library
import tkFont
import ttk #import the tkinter GUI library
#from PIL import Image, ImageTk
import time #import the time module
import os
import pytz
from pytz import timezone
from datetime import datetime
import ThermoData


# ### Configuration
# -  Some UI specific configuration items and names to create. 

# In[2]:

central = timezone('US/Central')

windowHeight = 240
windowWidth = 320


# ### The UI code

# In[12]:

####- The main elements (root window, title and frames)
rootWindow = Tk()
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
#rootWindow.rowconfigure(0, weight=1)05
#rootWindow.rowconfigure(1, weight=1)
#rootWindow.rowconfigure(2, weight=1)
#rootWindow.rowconfigure(3, weight=1)



contentFrame = ttk.Frame(rootWindow, padding=(5,5,5,5))
contentFrame.config(cursor="none") 
contentFrame.columnconfigure(0, weight=1)
contentFrame.columnconfigure(1, weight=1)
contentFrame.columnconfigure(2, weight=1)
contentFrame.columnconfigure(3, weight=1)
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

desTempVal = DoubleVar() # a varibale to hold the desired temperature
fanMode = StringVar() # a variable to hold the fan mode.
currTempVal = DoubleVar() # a variable to hold the current temperature
currHumidVal = DoubleVar() # a variable to hold the current humidity
currentDate = StringVar() # a variable to hold the current date.
currentTime = StringVar() # a variable to hold the current time.
airSelectionVal  = IntVar() # a variable to hold the current air selection.
#currentForecast  = StringVar() # a variable to hold the current forecast.
outsideTempVal  = IntVar() # a variable to hold the outside temp.
outsideHumidVal  = IntVar() # a variable to hold the outside humidity.


def getDBInformation():
    #retrieves the data from the DB and sets the values ot the UI components
    fcgQuery = ThermoData.getForecastData()
    currentForecast = (fcgQuery.fc_4dforecast)
    text_currentForecast.delete('1.0','5.0')
    text_currentForecast.insert('1.0',currentForecast)
    outsideTempVal.set(fcgQuery.fc_outsidetemp)
    outsideHumidVal.set(fcgQuery.fc_outsidehumidity)
    
    rtgQuery = ThermoData.getRealtimeData()
    currTempVal.set(rtgQuery.rt_currenttemp)
    currHumidVal.set(rtgQuery.rt_humidity)
    desTempVal.set(rtgQuery.rt_destemp)
    dbFanMode = rtgQuery.rt_fanmode
    if dbFanMode == 'H':
        airSelectionVal.set(0)
    if dbFanMode == 'C':
        airSelectionVal.set(1)
    if dbFanMode == 'F':
        airSelectionVal.set(2)
    if dbFanMode == 'O':
        airSelectionVal.set(3)
    if dbFanMode == 'A':
        airSelectionVal.set(4)
    utcTimeValue=(rtgQuery.rt_datetime)
    currentTimeValue = utcTimeValue.astimezone(central)
    currentDate.set(currentTimeValue.strftime('%a %b %d %Y'))
    currentTime.set(currentTimeValue.strftime('%I:%M %p'))
    rootWindow.after(5000,getDBInformation)


def updateDesTemp():
    rtuQuery = ThermoData.getRealtimeData()
    rtuQuery.rt_destemp = desTempVal.get()
    ThermoData.updateRealTimeData(rtuQuery)
    
def setAirMode():
    #print airSelectionVal.get()
    rtgQuery = ThermoData.getRealtimeData()
    if airSelectionVal.get() == 0:
        rtgQuery.rt_fanmode ='H'
        radio_airSelectionCool.configure(state='disabled')
        radio_airSelectionFan.configure(state='disabled')
    if airSelectionVal.get() == 1:
        rtgQuery.rt_fanmode = 'C'
        radio_airSelectionHeat.configure(state='disabled')
        radio_airSelectionFan.configure(state='disabled')
    if airSelectionVal.get() == 2:
        rtgQuery.rt_fanmode = 'F'
        radio_airSelectionHeat.configure(state='disabled')
        radio_airSelectionCool.configure(state='disabled')
    if airSelectionVal.get() == 3:
        rtgQuery.rt_fanmode = 'O'
        radio_airSelectionHeat.configure(state='normal')
        radio_airSelectionCool.configure(state='normal')
        radio_airSelectionFan.configure(state='normal')
    if airSelectionVal.get() == 4:
        rtGQuery.rt_fanmode = 'A'
    ThermoData.updateRealTimeData(rtgQuery)
    #print(airSelectionVal.get())

def quitUi():
    rootWindow.destroy()
    
def waitDelay():
    pass
    
###Define UI stuff

dTempFont = tkFont.Font(size=32)
valuesFont = tkFont.Font(size=16)
labelsFont = tkFont.Font(size=8)
forecastFont = tkFont.Font(size=8)



#Labels

labelAnchor = 'center'
label_currTemp = ttk.Label(contentFrame, text='Temp', font=labelsFont)
label_currTempVal = ttk.Label(contentFrame, textvariable=currTempVal, font=valuesFont, anchor=labelAnchor) 
label_currHumid = ttk.Label(contentFrame, text='Humidity', font=labelsFont)
label_currHumidVal = ttk.Label(contentFrame, textvariable=currHumidVal, font=valuesFont, anchor=labelAnchor) 
label_desiredTemp = ttk.Label(contentFrame, text='Desired', font=labelsFont)
label_desiredTempVal = ttk.Label(contentFrame, textvariable=desTempVal, font=valuesFont, anchor=labelAnchor)
label_currentTimeVal = ttk.Label(contentFrame, textvariable=currentTime, font=labelsFont, anchor=labelAnchor)
label_currentDateVal = ttk.Label(contentFrame, textvariable=currentDate, font=labelsFont, anchor=labelAnchor)
label_airSelection = ttk.Label(contentFrame, text='Air:')
label_outsideTempVal = ttk.Label(contentFrame, textvariable=outsideTempVal, font=valuesFont, anchor=labelAnchor, foreground="blue")
label_outsideHumidVal = ttk.Label(contentFrame, textvariable=outsideHumidVal, font=valuesFont, anchor=labelAnchor, foreground="blue")


text_currentForecast = Text(contentFrame,width=5, height=4, wrap='none', font=forecastFont)

#Buttons

btnWidth = 4

#btnRefreshTemp = ttk.Button(contentFrame, text='Refresh', command=getDBTempHumid)
btnQuitUi = ttk.Button(contentFrame, text='Exit', command=quitUi, width=btnWidth)


radio_airSelectionHeat= Radiobutton(contentFrame, text='Heat', variable=airSelectionVal, value=0, command = setAirMode, indicatoron=0)
radio_airSelectionCool= Radiobutton(contentFrame, text='Cool', variable=airSelectionVal, value=1,  command = setAirMode, indicatoron=0)
radio_airSelectionFan= Radiobutton(contentFrame, text='Fan', variable=airSelectionVal, value=2,  command = setAirMode, indicatoron=0)
radio_airSelectionOff= Radiobutton(contentFrame, text='Off', variable=airSelectionVal, value=3,  command = setAirMode, indicatoron=0)
radio_airSelectionAuto= Radiobutton(contentFrame, text='Auto', variable=airSelectionVal, value=4,  command = setAirMode, indicatoron=0)

#spinbox
spinUpdateDesTemp = Spinbox(contentFrame, from_ = 60.00, to = 99.00, textvariable = desTempVal, command = updateDesTemp, 
                            width =4,font=dTempFont, increment=.5, justify=CENTER, bg='light grey', relief='solid', 
                            state='readonly')
#flat, groove, raised, ridge, solid, or sunken




def gridStuff():
    ###Grid UI stuff
    #Content Frame
    contentFrame.grid(column=0, row=0, sticky='nsew')

    #labels
    lblpad_x = 5
    lblpad_y = 5
    lblcolspan = 1
    lblrowspan = 1
    lblsticky = (E,W)
    #label_currTemp.grid(row=0, column=0, columnspan=lblcolspan, rowspan=lblrowspan,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    label_currTempVal.grid(row=1, column=0, columnspan=lblcolspan, rowspan=lblrowspan,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    #label_desiredTemp.grid(row=0, column=1, columnspan=lblcolspan, rowspan=lblrowspan,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    #label_desiredTempVal.grid(column=2, row = 2, columnspan=lblcolspan, rowspan=lblrowspan,sticky=(N,S), pady=lblpad_y, padx=lblpad_x)
    #label_currHumid.grid(row=0, column=2, columnspan=lblcolspan, rowspan=lblrowspan,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    label_currHumidVal.grid(row=1, column=3, columnspan=lblcolspan, rowspan=lblrowspan,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    label_currentDateVal.grid(row=2, column=0, columnspan=4, rowspan=lblrowspan,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    label_currentTimeVal.grid(row=3, column=0, columnspan=4, rowspan=lblrowspan,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    
    label_outsideTempVal.grid(row=2, column=0, columnspan=lblcolspan, rowspan=2,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    label_outsideHumidVal.grid(row=2, column=3, columnspan=lblcolspan, rowspan=2,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    
    text_currentForecast.grid(row=5, column=0, columnspan=3, rowspan=lblrowspan,sticky=lblsticky, pady=lblpad_y, padx=lblpad_x)
    
    
    #Buttons and spinbox
    #button configs
    btnpad_x = 10
    btnpad_y = 10
    btncolspan = 1
    btnrowspan = 1
    btnsticky = (E,W)
    
    #btnRefreshTemp.grid(column=0, row=2, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    
    spinUpdateDesTemp.grid(row=1, column=1, columnspan=2, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    
    radio_airSelectionHeat.grid(row=4, column=0, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    radio_airSelectionCool.grid(row=4, column=1, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    radio_airSelectionFan.grid(row=4, column=2, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    radio_airSelectionOff.grid(row=4, column=3, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)
    
    btnQuitUi.grid(row=5, column=3, columnspan=btncolspan, rowspan=btnrowspan, sticky=btnsticky, pady=btnpad_y, padx=btnpad_x)

getDBInformation()
gridStuff()


rootWindow.mainloop()


# ###Dev Testing

# In[ ]:

#rtuQuery = ThermoData.getRealtimeData()


# In[ ]:

#float(rtuQuery.rt_destemp)


# In[ ]:

#ThermoData.updateRealTimeData(rtQuery)


# In[ ]:

#rtQuery = ThermoData.getRealtimeData()
#rtQuery.rt_currenttemp
#currentTime = rtuQuery.rt_datetime


# In[ ]:

#central = timezone('US/Central')
#print currentTime.astimezone(central)


# In[ ]:

#dir(currentTime)

