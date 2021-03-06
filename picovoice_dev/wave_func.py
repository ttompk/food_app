###
# pyaudio play or record source files
###

import pyaudio
import wave
import sys
import io

def AudioFile(resource_type, file_name, chunk = 1024):
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
    RESPEAKER_INDEX = 1  # run getDeviceInfo.py to get index = input device id
    
    try:
        resource_type = str(resource_type)
        file_name = str(file_name)
    except TypeError:
        print("Inputs are not the correct type.")

    # integer for chunk
    if not isinstance(chunk, int):
        print("Please enter an integer for 'chunk'.")
        sys.exit()
    
    # create pyaudio object
    p = pyaudio.PyAudio()          

    # perform either play or record then shutdown 
    if resource_type == 'play':
        stream = _play(p, file_name, chunk, RESPEAKER_INDEX)
    else:
        stream = _record(p, file_name, chunk, RESPEAKER_INDEX)
    # shutdown
    _close(p, stream)


def _play(p, file_name, chunk, RESPEAKER_INDEX):
    ''' create playback pyaudio object
    input: 
        p:   pyaudio object. 
        wf:  wave object.
        chunk:  int. 
    output:  plays wave file
    return:  nothing
    '''
    # open wave file
    try:
        wf = wave.open(file_name, 'rb')
    except FileNotFoundError:
        print("File was not found.")
        sys.exit()
    
    # derives params from wav file itself
    stream = p.open(
                    rate = wf.getframerate(),
                    format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    output = True,
                    output_device_index=RESPEAKER_INDEX)
    
    # read data
    data = wf.readframes(chunk) 
    
    # play stream
    while data:
        stream.write(data)
        data=wf.readframes(chunk)
    
    return stream


def _record(p, file_name, chunk, RESPEAKER_INDEX):
    ''' create record pyaudio object'''
    # constants. Update as needed to match picovoice
    RESPEAKER_RATE = 16000
    RESPEAKER_CHANNELS = 2 
    RESPEAKER_WIDTH = 2
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

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(RESPEAKER_CHANNELS)
    wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return stream


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
