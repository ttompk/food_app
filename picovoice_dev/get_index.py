###
# This code provided by seeed studios for 2-mic audio breakout board. 
# The code finds the device id for seeed studio card. Ouptut should looks similar to 
# below:  
# Input Device id  2  -  seeed-2mic-voicecard: - (hw:1,0).
# The number "2" in this case is used in the record.py file at "RESPEAKER_INDEX = 2"  
# On the pi zero it was "Input Device id  1  -  seeed-2mic-voicecard: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 (hw:1,0)"
###

import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

