# Voice Command Detection  

#### Feature  
Voice detection  

#### Purpose 
The purpose of this feature is to add voice command detection to the food_app product. Voice detection is being added to improve the utility of the product by providing hands-free operation.    

#### Solution 
The feature will utilize a two stage approach. First, the system is always listening for a wake word. Secondly, upon wake word identification the feature will listen for an action command statement. This is similar to saying "Alexa, set a time for 5 minutes".     

__Key Requirements:__   
- All voice detection (inference) must be performed locally on the product - no call to cloud  
- Include wake word detection followed by command detection.    
- Provide an audible response to the spoken command via internal speaker.  
- Functions to be performed:  
  * Print labels:  'open date', 'today's date', etc.  
  * Set a timer   


### Picovoice
One solution is to use picovoice. Picovoice is the name of a company, platform, and sdk.  Picovoice has developed an inference engine that works on the raspberry pi for both wake word and 'contextual' intent identification.  The tool can be implemented with python (among many other languages). Both sdks - wake word and intent identification - ship with default examples for develpment with the possibil;ity to create your own command and wake word identification.  

From Picovoice:
'Picovoice enables enterprises to innovate and differentiate rapidly with private voice AI. Build a unified AI strategy around your brand and products with our speech recognition and Natural-language understanding (NLU) technologies.'


Picovoice wake word sdk = 'porcupine'.
Picovoice intent sdk = 'rhino'.  

#### Dependencies for picovoice on Pi Zero  

Picovoice requires alsa and pyaudio be installed on the Pi Zero.  
- ALSA : ships with RpiOS Buster.   
- Pyaudio : needs to be installed on Pi Zero. Requires pyaudio, which requires portaudio. 
  * __PortAudio Install:__ 
  * `sudo apt-get remove libportaudio`  
  * `sudo apt-get install libasound-dev`    
  * `wget http://files.portaudio.com/archives/pa_stable_v190600_20161030.tgz` 
  * `tar -xvzf pa_stable_v190600_20161030.tgz`  
  * `cd portaudio`  
  * `./configure`  
  * `make`  
  
  * __Pyaudio Install:__  
  * `pip install PyAudio`    

Try out pyaudio by running the following files:
1. Run 'get_index.py' to identifiy number of respeaker card. 
2. Input the hardware number in 'record.py' then run.  
3. 'record0.py' is similar to 'record.py' but condenses the input channel to n=1.  
 

Helpful port audio refs:  
https://app.assembla.com/wiki/show/portaudio/Platforms_RaspberryPi  
http://files.portaudio.com/download.html  


#### Picovoice   
Picovoice has produced a demo especially designed for the 2-mic respeaker board. The demo flashes LED lights on the resepeaker board.  

__Install picovoice demo:__  
`pip install pvrespeakerdemo`  
`picovoice_respeaker_demo`   

Running the above demo install will install both porcupine and rhino.    

rhino_dev.py is a basic tempate for running rhino. There are default templates provided by picovoice '/contexts'.  

 


 
 

 


