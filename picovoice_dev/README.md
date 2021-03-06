# Voice Command Detection  

#### Feature  
Voice detection  

#### Purpose 
The purpose of this feature is to add voice command detection to the food_app product. Voice detection is being added to improve the utility of the product by providing hands-free operation.    

#### Solution 
The feature will utilize a two stage approach. First, the system is always listening for a wake word. Secondly, upon wake word identification the feature will listen for an action command statement. This is similar to saying "Alexa, set a time for 5 minutes".     

__Key Requirements:__   
- All voice detection (inference) must be performed locally on the product - no call to cloud  
- Include wake word detection followed by command detection.    
- Provide an audible response to the spoken command via internal speaker.  
- Functions to be performed:  
  * Print labels:  'open date', 'today's date', etc.  
  * Set a timer   


### Picovoice
One solution is to use picovoice. Picovoice is the name of a company, platform, and sdk.  Picovoice has developed an inference engine that works on the raspberry pi for both wake word and 'contextual' intent identification.  The tool can be implemented with python (among many other languages). Both sdks - wake word and intent identification - ship with default examples for develpment with the possibil;ity to create your own command and wake word identification.  


  
 
 

 


