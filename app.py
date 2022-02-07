import os
import yaml
import androidhelper as android

path_file = os.path.abspath(__file__)
path = os.path.dirname(path_file)

#Classe para manipular aplicativos
class App:
    droid = android.Android()
    
    def __init__(self):
        pass

    def abrir(self, packageName, activity):
      self.droid.startActivity('android.intent.action.MAIN', None, None, None, False, packageName, activity)
     
    def listaapps(self):
      os.chdir(path)
      data = yaml.safe_load(open('./DB/apps.yml', 'r', encoding='utf-8').read())
      return data['apps']