#Usar la API de Have I been pwn?
import requests
import json
import logging
import getpass

# Solicitar la API key de manera segura
api_key = getpass.getpass("Ingresa tu API key: ") #API key: "ec1e2ebed1754f1b8c00f2b90aa15906"

# Definir headers de la petición
headers = {
    'content-type': 'application/json',
    'api-version': '3',
    'User-Agent': 'Python',
    'hibp-api-key': api_key
}

# Solicitar correo electrónico a verificar
email = input("Ingresa el correo a investigar: ")

# URL de la API de Have I Been Pwned
url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"

# Configurar el logging para errores
logging.basicConfig(filename='hibpERROR.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.ERROR)

try:
    # Realizar la solicitud a la API
    response = requests.get(url, headers=headers)
    response.raise_for_status()

except requests.exceptions.HTTPError as http_err:
    if response.status_code == 401:
        print("API key inválida o no autorizada.")
    else:
        print(f"Error HTTP: {http_err}")

except Exception as err:
    print(f"Ocurrió un error: {err}")

else:
    # Procesar la respuesta
    breaches = response.json()
    
    if breaches:
        with open('reporte_filtraciones.txt', 'w') as f:
            f.write(f"Filtraciones encontradas para {email}:\n\n")
            for breach in breaches:
                f.write(f"Nombre: {breach['Name']}\n")
                f.write(f"Dominio: {breach['Domain']}\n")
                f.write(f"Fecha de filtración: {breach['BreachDate']}\n")
                f.write(f"Descripción: {breach['Description']}\n")
                f.write("\n-------------------------------------\n")
        print(f"Se encontraron filtraciones. Revisa 'reporte_filtraciones.txt'.")
    else:
        print(f"No se encontraron filtraciones para {email}.")

finally:
    print("Proceso completado")