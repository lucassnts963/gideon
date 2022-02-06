import core
from funcionalidades import VozByAndroidHelper
import os

os.system('clear')

voz = VozByAndroidHelper()

texto = voz.escute()
print(texto)