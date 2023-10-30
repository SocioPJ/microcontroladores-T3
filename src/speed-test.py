
import speedtest
import requests



st = speedtest.Speedtest(secure=True)


while True:
 g = requests.get('https://industrial.api.ubidots.com/api/v1.6/devices/raspberry-pi/button/lv/?token=BBFF-xBmJ1Kw6JkKu8qPcSkm2gYvYLuRHKw')
 #print(g.content)
 if g.content == b'1.0':
  try:
   print(f'Iniciando Medição...')
   st.get_best_server()
   payload = {
   'download': round(st.download() / 1000000, 2),
   'upload': round(st.upload() / 1000000, 2),
   'ping': round(st.results.ping, 2)}
   r = requests.post('https://industrial.api.ubidots.com/api/v1.6/devices/raspberry-pi/?token=BBFF-xBmJ1Kw6JkKu8qPcSkm2gYvYLuRHKw',data=payload)
   print('Medição finalizada!')
  except Exception as identifier:
   print(identifier)
 else:
  print('Botão desligado')