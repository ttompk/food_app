from wave_func import AudioFile
import os

wav_file = 'piano2.wav'
os.system(f'aplay -Dhw:1 -d 10 ~/food_app/picovoice_dev/{wav_file}')

# this works but takes a long time to load
# makes a popping sound after file ran
#AudioFile("play", "/home/pi/food_app/picovoice_dev/piano2.wav")
