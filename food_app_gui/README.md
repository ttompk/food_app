# Kivy Front End

Building a gui for food app.  What is Kivy. Why use Kivy. 

### Install Kivy 
Instruction to install kivy is stated in project root readme (or move here).  

### Kivy Overview

When using Kivy there are three files that need creation/adjustment on a Pi Zero.  
1. config.ini - The first is a config file that sits at _~/.kivy/config.ini_.  This file is used to set parameters for how a kivy app interacts with the screen hardware.   
2. <app>.py - This file runs the app and contains functions for handling widget inputs (buttons, sliders, etc).  
3. <my>.kv - This is a yaml file that contains the layout of the buttons. It's similar to a _.html_ file.  


## Food App Gui
The gui should perform the following functions: 
- select type of label to print 
- change system settings

### Label Types
There are three label types:  
1. When Food Expires - this label lets one select how long until the food expires and the type of food (veggie, meat, dairy)  
2. Opening Date - this label prints the date somehting was opened.  
3. Today's Date - prints a label with today's date. This cculd be used to label leftovers or any general purpose.  


### Settings  
The app should have a button to access the settings page.  The settings include:  
1. Turn wifi on/off
2. Edit wifi settings - input wifi ssid and password  
3. Edit sleep duration - change how long the device screen stays on after using  
4. Select speaker volume - change the loudness of the attached speaker  


## Screens  
1. Main - the primary screen to reach all other screens.  
  * Expiriry button
  * Opened button  
  * Today's Date button
  * Settings button     
- Days - Number of days until food expires.
  * Number buttons 1-8
  * Go Back button  
- Food Type - Select type of food  
  * Veggie button
  * Meat button  
  * Dairy button  
  * Go back button    
- Settings 
  * Wifi On/Off radio slider button 
  * Edit Wifi Settings button  
  * Edit Sleep Duration button 
  * Speaker Volume slider (or button)   
