#Integrantes del equipo
#Luis Mael Treviño Mares
#Diego Fernando Betancourt Soto
#Carlos Sebastian Barceinas Olascoaga

import subprocess
import re

# Definir los puertos estándar
puertos_estandar = [22, 25, 80, 465, 587, 8080]

# Ejecutar el script de Bash y capturar la salida
try:
    resultado_bash = subprocess.run(['./monitor_conexiones.sh'], capture_output=True, text=True, check=True)
    conexiones = resultado_bash.stdout.splitlines()
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el script de Bash: {e}")
    exit(1)

# Analizar las conexiones capturadas por el script de Bash
conexiones_sospechosas = []
for conexion in conexiones:
    # Usar una expresión regular para extraer el número de puerto
    puerto = re.search(r':(\d+)', conexion)
    if puerto:
        numero_puerto = int(puerto.group(1))
        # Verificar si el puerto no está en la lista de puertos estándar
        if numero_puerto not in puertos_estandar:
            conexiones_sospechosas.append(conexion)

# Guardar las conexiones sospechosas en un archivo
if conexiones_sospechosas:
    with open('conexiones_sospechosas.txt', 'w') as archivo:
        for conexion in conexiones_sospechosas:
            archivo.write(f"{conexion}\n")
    print("Conexiones sospechosas identificadas y guardadas en 'conexiones_sospechosas.txt'.")
else:
    print("No se encontraron conexiones sospechosas.")