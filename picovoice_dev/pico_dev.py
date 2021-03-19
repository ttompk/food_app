import os
import sys
from threading import Thread

import pyaudio
from picovoice import Picovoice

'''
Picovoice engines require 16-bit 16kHz linearly-encoded PCM (single-channel) audio.
'''

class PicovoiceDemo(Thread):
    '''
    
    '''
    def __init__(
            self,
            keyword_path,
            context_path,
            porcupine_sensitivity=0.75,
            rhino_sensitivity=0.25):  

        super(PicovoiceDemo, self).__init__()

        def inference_callback(inference):
            return self._inference_callback(inference)
        
        self._picovoice = Picovoice(
            keyword_path=keyword_path,
            wake_word_callback=self._wake_word_callback,
            context_path=context_path,
            inference_callback=inference_callback,
            porcupine_sensitivity=porcupine_sensitivity,
            rhino_sensitivity=rhino_sensitivity)
        
        self._context = self._picovoice.context_info

    # @staticmethod
    # They're main purpose is to contain logic pertaining to 
    # the class, but that logic should not have any need for 
    # specific class instance data.
    @staticmethod
    def _wake_word_callback():
        print('[wake word]\n')

    def _inference_callback(self, inference):
        print("Inference Callback ")
        print('{')
        print(f"  is_understood : {'true' if inference.is_understood else 'false'}"
        
        if inference.is_understood:
            print(f" intent : {inference.intent}")
            if len(inference.slots) > 0:
                print('    slots : {')
                for slot, value in inference.slots.items():
                    print(f"    {slot} : {value}")
                print('    }')
        print('}\n')

        if inference.is_understood:
            if inference.intent == 'turnLights':  # replace this with setTimer
                if inference.slots['state'] == 'off': 
                    # run a function
                    #default = self._set_color((0, 0, 0))
                    pass
                else: 
                    # run another function
                    #default = self._set_color(COLORS_RGB[self._color])
                    pass
            elif inference.intent == 'changeColor':
                self._color = inference.slots['color']
                self._set_color(COLORS_RGB[self._color])
            else:
                raise NotImplementedError()
    
    # This method runs after picovoicedemo object instantiation. 
    def run(self):
        pa = None
        audio_stream = None

        try:
            pa = pyaudio.PyAudio()

            # frame_length default = 512 
            audio_stream = pa.open(
                rate = self._picovoice.sample_rate,
                channels = 1,
                format = pyaudio.paInt16,
                input = True,
                frames_per_buffer=self._picovoice.frame_length)
            
            print(self._context)

            print('[Listening ...]')

            while True:
                pcm = audio_stream.read(self._picovoice.frame_length)
                pcm = struct.unpack_from("h" * self._picovoice.frame_length, pcm)

                self._picovoice.process(pcm)
            
            except KeyboardInterrupt:
                sys.stout.write('\b' * 2)
                print("Stopping ...")
            
            finally:
                if audio_stream is not None:
                    audio_stream.close()

                if pa is not None:
                    pa.terminate()
                
                self._picovoice.delete()

def main():
    # instantiate PicovoiceDemo
    # .ppn is porcupine wake words 
    #       - how to make custom wake word?
    # .rhn is rhino intent files - respeaker board came with .rhn file 
    #       - make custom rhino via console 
    #       - how to do locally? 
    
    # Select wake word file here: 
    wake_file = os.path.join(os.path.dirname(__file__), 'picovoice_raspberry-pi.ppn')
    
    # Select rhino context file here:
    #rhino_file = os.path.join(os.path.dirname(__file__), 'respeaker_raspberry-pi.rhn')
    #rhino_file = os.path.join(os.path.dirname(__file__), 'contexts/alarm_raspberry-pi.rhn')
    rhino_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'contexts/alarm_raspberry-pi.rhn')
    
    o = PicovoiceDemo(
        wake_file,
        rhino_file)
    o.run()

if __name__ == '__main__':
    main()
