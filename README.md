# food_app


## Hardware
raspberry pi
touchscreen running kivy app
sound card with audio input/output

### Hardware Install
## 7-inch Touchscreen  
Install using this [ref](http://www.lcdwiki.com/7inch_HDMI_Display-C#Step_3.2C_Drive_the_5inch_HDMI_Display-B_with_the_Raspberry_Pi)  

## Sound Card Install 
see [Voice Command](https://github.com/ttompk/voice_command) repo for installation directions.  


## Software

### Touchscreen App
The touchscreen app runs using the Kivy package.  The screen can be edited to add buttons, etc and actions related to button pushes.   
  
To run the app:  
`python /food_app_gui/app_food_beta.py`  


### Installing Kivy
Installing Kivy on raspberry pi zero was a pain as the documentation is limited.  

This [ref](http://mattrichardson.com/kivy-gpio-raspberry-pi-touch/index.html) was helpful.  

Add this to '~/.kivy/config.ini' on Pi Zero:   
`mouse = mouse`  
`mtdev_%(name)s = probesysfs,provider=mtdev`  
`hid_%(name)s = probesysfs,provider=hidinput`  


### Wake word using Picovoice  
Picovoice:  
_'Picovoice enables enterprises to innovate and differentiate rapidly with private voice AI. Build a unified AI strategy around your brand and products with our speech recognition and Natural-language understanding (NLU) technologies.'_  

There is a demo especially designed for the 2-mic respeaker board.  

Install picovoice demo:  
`pip install pvrespeakerdemo`  
`picovoice_respeaker_demo`  


### SQLite db
Saving the food entries in a db. Using SQLite for now but ideally move to nosql document storage. Mongodb is not available for pi zero excpet for an older version that is may not be compatible. Will need to investigate the use of key-value pairs in SQLite.  

Install:  
`sudo apt-get install sqlite3`  

db name =  foodDB.db  
path =     /home/pi/  

Table: label  
* id  integer  primary key  not null,
* entry_time  text not null,  
* entry_method  text  not null,  
* food_type  text,  
* expire_date  text,  
* pic  blob,  
* pred_food  text,  
* prob_food  real  





