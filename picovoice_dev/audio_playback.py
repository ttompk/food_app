# audio_playback.py

###
# plays and records audio from command line on Pi Zero
###

import os

# NOTE: # run getDeviceInfo.py to get index = input device id

def play_file(wav_file='', RESPEAKER_INDEX=1):
    if wav_file == '':
        wav_file = 'piano2.wav'
  
    # play the sound file using command line
    os.system(f'aplay -Dhw:{RESPEAKER_INDEX} -d 10 ~/food_app/picovoice_dev/{wav_file}')

def record_file(wav_file='', nseconds=5, RESPEAKER_INDEX=1):
    if wav_file=='':
        wav_file = 'test_record.wav'
    # record sound
    print(" * Recording ... ")
    os.system(f'arecord -f S16_LE -d {nseconds} -r 16000 -Dhw:{RESPEAKER_INDEX} ~/food_app/picovoice_dev/{wav_file} -c 2')
    print(" * Recording Ended" )


# this works but takes a long time to load
# makes a popping sound after file ran
#from wave_func import AudioFile
#AudioFile("play", "/home/pi/food_app/picovoice_dev/piano2.wav")

if __name__=='__main__':
    wav_file = input("File name (empty = default): ")
    resp = input("'play' or 'record: ")
    if resp == 'play':
        play_file(wav_file)
    elif resp == 'record':
        nseconds = input('n seconds (empty = 5): ')
        if nseconds == '':
            nseconds = 5
        record_file(wav_file, nseconds)
    else:
        print("play or record required")