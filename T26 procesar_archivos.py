#Integrantes del equipo
#Luis Mael Treviño Mares
#Diego Fernando Betancourt Soto
#Carlos Sebastian Barceinas Olascoaga

import subprocess
import openpyxl
from io import StringIO
import csv 

# Ejecutar el script de PowerShell
try:
    result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "C:\\Users\\LUIS\\OneDrive\\Documentos\\Mael\\monitor_servicios.ps1"], 
                            capture_output=True, text=True, check=True)
    
    # Capturar la salida del script de PowerShell
    output = result.stdout

    # Leer la salida como CSV
    csv_reader = csv.reader(StringIO(output))
    headers = next(csv_reader)  # Obtener encabezados

    # Crear un nuevo archivo de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Servicios"

    # Escribir encabezados en Excel
    ws.append(headers)

    # Escribir los datos en Excel
    for row in csv_reader:
        ws.append(row)

    # Guardar el archivo de Excel
    wb.save(r"C:\Users\LUIS\OneDrive\Documentos\Mael\servicios_sistema.xlsx")
    print("Datos de los servicios registrados en 'servicios_sistema.xlsx' con éxito.")

except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el script de PowerShell: {e}")
except Exception as e:
    print(f"Error procesando los datos: {e}")