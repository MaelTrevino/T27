import requests
import json
import logging
import getpass
import six
import argparse
import sys
 
# Verificación de la versión de Python
if not six.PY3:
    raise Exception("Este script debe ejecutarse en Python 3.")
 
# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 
def v_correo(email, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        'User-Agent': 'HIBP Python Script',
        'hibp-api-key': api_key,
    }
 
    try:
        response = requests.get(url, headers=headers)
 
        if response.status_code == 200:
            try:
                breaches = response.json()
                return breaches
            except json.JSONDecodeError:
                logging.error("No se pudo decodificar la respuesta JSON.")
                return []
        elif response.status_code == 404:
            logging.info("No se encontraron filtraciones en el correo.")
            return []
        else:
            logging.error(f"ERROR al comunicarse con la API: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"ERROR al realizar la solicitud: {str(e)}")
        sys.exit(1)
 
# Generar reporte con lo encontrado
def generar_reporte(email, breaches):
    report_file = f"reporte_{email.replace('@','_at_')}.txt"
 
    with open(report_file, 'w') as file:
        file.write(f"Reporte de filtraciones para: {email}\n\n")
        if breaches:
            for breach in breaches:
                file.write(f"Nombre de la filtración: {breach['Name']}\n")
                file.write(f"Fecha de la filtración: {breach['BreachDate']}\n")
                file.write(f"Descripción: {breach['Description']}\n\n")
            logging.info(f"Reporte generado: {report_file}")
        else:
            file.write("No se encontraron filtraciones.\n")
            logging.info(f"No se encontraron filtraciones. Reporte generado: {report_file}")
 
# Hacer solicitud de la API de una manera segura
def main():
    api_key = getpass.getpass(prompt="Introduce tu API Key de 'Have I Been Pwned': ").strip()  # API key limpia
 
    # Manejo de parámetros con argparse
    parser = argparse.ArgumentParser(description="Verificar si un correo electrónico ha sido filtrado")
    parser.add_argument('email', type=str, help='Correo electrónico a verificar')
    args = parser.parse_args()
 
    email = args.email
 
    # Llamada a la función para verificar el correo
    breaches = v_correo(email, api_key)
 
    # Generar reporte
    generar_reporte(email, breaches)
 
if __name__ == '__main__':
    main()