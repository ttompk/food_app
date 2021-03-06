import os
import sys
from threading import Thread

import pyaudio
from picovoice import Picovoice

class PicovoiceDemo(Thread):
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
        