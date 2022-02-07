# Ações dos comandos
import datetime

from app import App

app = App()

def getTime():
  agora = datetime.datetime.now()
  hora = agora.hour
  minu = agora.minute
  
  resposta = 'São {} horas e {} minutos'.format(hora, minu)
  return resposta

def getDate():
  agora = datetime.datetime.now()
  dia = agora.day
  mes = agora.month
  ano = agora.year
  
  resposta = 'Hoje é dia {} do mês {} de {}'.format(dia, mes, ano)
  return resposta

def openApp(entrada):
  for aplicativo in app.listaapps():
    name = aplicativo['app']['name']
    packageName = aplicativo['app']['packageName']
    activity = aplicativo['app']['activity']
    n_lower, e_lower = name.lower(), entrada.lower()
    isEqual = (n_lower == e_lower)
    if isEqual:
      app.abrir(packageName, activity)

#Por enquanto o metodo retorna apenas uma mensagem estática
def getWeather():
  return 'Ainda não consigo mostrar a previsão do tempo.'
  