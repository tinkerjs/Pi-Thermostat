#!/usr/bin/python3

import subprocess
import os

os.chdir('/thermostat/')
#print(os.getcwd())


subprocess.call(['ipython', 'notebook', '--no-browser' ,
					'--colors=LightBG', 
					'--ip=192.168.1.19',
					'--port=8889', 
					])