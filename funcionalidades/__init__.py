import os
import json
import subprocess
import androidhelper as android

class VozByTermux:
  
  def __init__(self):
    pass

  def fale (self, texto):
    subprocess.run(['termux-tts-speak', texto])
  
  def escute (self):
    result = json.loads(subprocess.getoutput('termux-dialog speech'))
    return result

class VozByAndroidHelper:
    droid = android.Android()
    
    def __init__(self):    
            pass
            
    def  fale(selt, texto):
        self.droid.ttsSpeak(texto)
        
    def escute(self):
        (id, result, error) = self.droid.recognizeSpeech('fale')
        return result
    