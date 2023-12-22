import requests
from googletrans import Translator
import os

tokenn = os.environ.get('OPENWEATHERMAP_TOKEN')

lat = -8.05428
lon = -34.8813

url1 = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={tokenn}"

try:
    # Fazendo a solicitação GET
    response = requests.get(url= url1)

    # Verificando se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Se a resposta estiver em formato JSON, você pode acessar os dados assim:
        dados = response.json()
        temperatura_atual = dados['current']['temp']
        temperatura_em_ceusios = temperatura_atual - 273.15
        print(f"Temperatura Atual: {round(temperatura_em_ceusios, 2)}°C")

        # Obtendo a primeira previsão
        primeira_previsao = dados['daily'][0]['temp']
        print(f"Primeira Previsão: {primeira_previsao}°C")

        descricao_tempo_amanha = dados['daily'][1]['weather'][0]['description']
        print(f"Previsão do Tempo para Amanhã: {descricao_tempo_amanha}")

        
        translator = Translator()
        descricao_traduzida = translator.translate(descricao_tempo_amanha, dest='pt')
        print(f"Tradução: {descricao_traduzida.text}")
        
    else:
        print("Erro na solicitação. Código de status:", response.status_code)

except Exception as e:
    print("Erro durante a solicitação:", str(e))
