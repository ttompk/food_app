###
# pyaudio play or record.
###

import pyaudio
import wave
import sys

class AudioFile:
    '''
    Play or record a wav file.  
    '''

    def __init__(self, resource_type, file, chunk = 1024):
        ''' Init audio stream 
        input:  
            resource_type:  str. States whether to play or record the file. Either 'play' or 'record'
            file:           str. name of sound file to play/record.
            chunk:          int. 
        output:  either sound (play) or creatation of wav file (record)
        depends:  pyaudio, sys
        returns:  none
        ''' 
        try:
            self.resource_type = str(resource_type)
            self.file = str(file)
        except TypeError:
            print("Inputs are not the correct type.")

        # integer for chunk
        if not isinstance(self.chunk, int):
            print("Please enter an integer for 'chunk'.")
            sys.exit()

        # open wave file
        try:
            self.wf = wave.open(file, 'rb')
        except FileNotFoundError:
            print("File was not found.")
            sys.exit()
        
        # perform either play or record then shutdown
        self.p = pyaudio.PyAudio()          # create pyaudio object
        if resource_type == 'play':
            self.play()
        else:
            self.record()
        # shutdown
        self.close()

    def play(self):
        ''' create playback pyaudio object'''
        # derives params from wav file itself
        self.stream = self.p.open(
                        rate = self.wf.getframerate(),
                        format = self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels = self.wf.getnchannels(),
                        output = True)
        
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def record(self):
        ''' create record pyaudio object'''
        # constants. Update as needed to match picovoice
        RESPEAKER_RATE = 16000
        RESPEAKER_CHANNELS = 2 
        RESPEAKER_WIDTH = 2
        RESPEAKER_INDEX = 1  # run getDeviceInfo.py to get index = input device id
        RECORD_SECONDS = 5
        
        self.stream = self.p.open(
                        rate=RESPEAKER_RATE,
                        format=p.get_format_from_width(RESPEAKER_WIDTH),
                        channels=RESPEAKER_CHANNELS,
                        input=True,
                        input_device_index=RESPEAKER_INDEX,)
        
        print("* recording")

        frames = []

        for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

    def close(self):
        ''' Graceful shutdown '''
        self.stop_stream()
        self.stream.close()
        self.p.terminate()


'''
# Usage example for pyaudio
AudioFile("play", "piano2.wav")
'''
