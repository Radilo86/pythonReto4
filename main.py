"""
    Ejercicio 4
    Enunciado: Utilizando la API de https://openweathermap.org/ y realizando una
    petición a api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key},
    obtén la temperatura máxima y mínima, para la ciudad que proporcione el usuario.

    Objetivo:
        - Aprender a utilizar librerías externas (en este caso, requests)
        - Manipular el resultado de la petición (JSON)
"""
# Importamos la libreria requests que nos permite recibir contenido de una web o realizar peticiones a APIs
import requests
import json

# Example Url: https://api.openweathermap.org/data/2.5/weather?q=yecla&appid=5318aa4952f008887a523972a6efdd57

url = "https://api.openweathermap.org/data/2.5/weather?q="
apiKey = "&appid=fa6105160ed9c8da7afa4e80bfb0cd84"
sistemaDecimal = "&units=metric"
ciudad = input("Introduce la ciudad: ")

urlCompleta = url + ciudad + apiKey + sistemaDecimal;
# print(urlCompleta)
peticion = requests.get(urlCompleta)

# print(peticion.text) # Muestra los datos de la peticion

# Cargamos los datos de formato Json en la variable datos para posteriormente "formatearlos"
datos = json.loads(peticion.content)

# print(datos)
print("La temperatura máxima es: ", datos['main']['temp_max'], "ºC")
print("La temperatura mínima es: ", datos['main']['temp_min'], "ºC")
