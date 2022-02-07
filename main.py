import core
from funcionalidades import VozByAndroidHelper
import os

os.system('clear')

voz = VozByAndroidHelper()

core.openApp('netflix')

while True:
  #entrada = voz.escute()
  entrada = input ('User: ')
  voz.fale(entrada)