###
# pyaudio play or record source files
###

import pyaudio
import wave
import sys

def AudioFile(resource_type, file, chunk = 1024):
    '''
    Play or record a wav file.  
    input:  
        resource_type:  str. States whether to play or record the file. Either 'play' or 'record'
        file:           str. name of sound file to play/record.
        chunk:          int. 
    output:  either sound (play) or creatation of wav file (record)
    depends:  pyaudio, sys
    returns:  none
    ''' 
    try:
        resource_type = str(resource_type)
        file = str(file)
    except TypeError:
        print("Inputs are not the correct type.")

    # integer for chunk
    if not isinstance(chunk, int):
        print("Please enter an integer for 'chunk'.")
        sys.exit()

    # open wave file
    try:
        wf = wave.open(file, 'rb')
    except FileNotFoundError:
        print("File was not found.")
        sys.exit()
    
    # perform either play or record then shutdown
    p = pyaudio.PyAudio()          # create pyaudio object
    if resource_type == 'play':
        _play(p, wf, chunk)
    else:
        record(p, stream, chunk)
    # shutdown
    close(p, stream)


def _play(p, wf, chunk):
    ''' create playback pyaudio object
    input: 
        p:   pyaudio object. 
        wf:  wave object.
        chunk:  int. 
    output:  plays wave file
    return:  nothing
    '''
    # derives params from wav file itself
    stream = p.open(
                    rate = wf.getframerate(),
                    format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    output = True)
    
    """ Play entire file """
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)


def _record(p, stream, chunk):
    ''' create record pyaudio object'''
    # constants. Update as needed to match picovoice
    RESPEAKER_RATE = 16000
    RESPEAKER_CHANNELS = 2 
    RESPEAKER_WIDTH = 2
    RESPEAKER_INDEX = 1  # run getDeviceInfo.py to get index = input device id
    RECORD_SECONDS = 5
    
    stream = p.open(
                    rate=RESPEAKER_RATE,
                    format=p.get_format_from_width(RESPEAKER_WIDTH),
                    channels=RESPEAKER_CHANNELS,
                    input=True,
                    input_device_index=RESPEAKER_INDEX,)
    
    print("* recording")

    frames = []

    for i in range(0, int(RESPEAKER_RATE / chunk * RECORD_SECONDS)):
        data = stream.read(chunk)
        frames.append(data)

    print("* done recording")


def _close(p, stream):
    ''' Graceful shutdown '''
    stream.stop_stream()
    stream.close()
    p.terminate()


'''
# Usage example for pyaudio
import wave_func
AudioFile("play", "/Users/kenwyn/datascience/food_app/picovoice_dev/piano2.wav")
'''
