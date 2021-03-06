### 
# rhino dev file
###

# initial code here: https://github.com/Picovoice/rhino  

import pvrhino

# set variables for context file: '/absolute/path/to/context'
Path_To_Context = 'home/pi/food_app/picovoice_dev/context'  # default' 
Sample_Rate = 16000   # default 16000  
Frame_Length = 521    # default 512  


handle = pvrhino.create(context_path = Path_To_Context)

def get_next_audio_frame():
    pass

while True:
    is_finalized = handle.process(get_next_audio_frame())

    if is_finalized:
        inference = handle.get_inference()
        if not inference.is_understood:
            # add code to handle unsupported commands
            # play wav file saying: "I'm sorry, I didn't understand the command."
            pass
        else:
            intent = inference.intent
            slots = inference.slots
            # add code to take action based on inferred intent and slot values


# Finally, when done be sure to explicitly release the resources using:
handle.delete()
