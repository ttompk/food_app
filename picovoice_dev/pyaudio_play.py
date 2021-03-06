from wave_func import AudioFile
import os

os.system('aplay -Dhw:1 -d 10 ~/food_app/picovoice_dev/piano2.wav')


#AudioFile("play", "/Users/kenwyn/datascience/food_app/picovoice_dev/piano2.wav")
AudioFile("play", "/home/pi/food_app/picovoice_dev/piano2.wav")
