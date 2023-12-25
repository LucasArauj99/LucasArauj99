import requests
from googletrans import Translator
import os
from geopy.geocoders import OpenCage

def converso_de_temperatuda(temperatura):
    #transforma kelvin para celsius
    return round((temperatura - 273.15), 2)


def temperatura_atual(): 
    temperatura_atual = converso_de_temperatuda(dados['current']['temp'])
    #temperatura_em_ceusios = temperatura_atual - 273.15
    print(f"Temperatura Atual: {temperatura_atual}°C")
    
def previsao():
    descricao_tempo_amanha = dados['daily'][1]['weather'][0]['description']
    temp_minima = converso_de_temperatuda(dados['daily'][1]['temp']['min'])
    temp_maxima = converso_de_temperatuda(dados['daily'][1]['temp']['max'])
    translator = Translator()
    descricao_traduzida = translator.translate(descricao_tempo_amanha, dest='pt').text
    print(f"Previsão do tempo para amanhã: \n{descricao_traduzida},"
         f"com a temperatura podendo variar de {temp_minima}°C até {temp_maxima}°C")

try:

    tokenn = os.environ.get('OPENWEATHERMAP_TOKEN')
    token_geo = os.environ.get('geo_token')
    cidade = str(input("Qual a cidade que deseja ver: "))
    estado = str(input('Qual o estado: '))
    geocoder = OpenCage(token_geo)
    location = geocoder.geocode(f"{cidade}, {estado}")
    lat, lon = location.latitude, location.longitude

    url1 = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={tokenn}"
    # Fazendo a solicitação GET
    response = requests.get(url=url1)

    # Verificando se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        dados = response.json()
        temperatura_atual()

        
        #primeira_previsao = dados['daily'][0]['temp']
        previsao()
    else:
        print("Erro na solicitação. Código de status:", response.status_code)

except Exception as e:
    print("Erro durante a solicitação:", str(e))