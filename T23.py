#INTEGRANTES
#Luis Mael Treviño Mares
#Diego Fernando Betancourt Soto
import pyautogui
import subprocess
from datetime import datetime
import sys

def captura_pantalla(custom_name=None):
    try:
        # Obtener la fecha y hora actual
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Usar el nombre personalizado o generar uno basado en la fecha y hora
        screenshot_filename = f"{custom_name or 'screenshot_' + timestamp}.png"
        
        # Capturar la pantalla
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_filename)
        
        print(f"Captura de pantalla guardada como {screenshot_filename}")
    except Exception as e:
        print(f"Error al capturar la pantalla: {e}", file=sys.stderr)

def registro_procesos(custom_name=None):
    try:
        # Obtener la fecha y hora actual
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Usar el nombre personalizado o generar uno basado en la fecha y hora
        tasklist_filename = f"{custom_name or 'tasklist_' + timestamp}.txt"
        
        # Ejecutar el comando tasklist
        result = subprocess.run(["tasklist"], capture_output=True, text=True, shell=True)
        
        # Verificar si la ejecución fue exitosa
        if result.returncode == 0:
            with open(tasklist_filename, "w") as file:
                file.write(result.stdout)
            print(f"Lista de procesos guardada como {tasklist_filename}")
        else:
            print(f"Error al ejecutar el comando tasklist: {result.stderr}", file=sys.stderr)
    except Exception as e:
        print(f"Error al capturar la lista de procesos: {e}", file=sys.stderr)

def main():
    # Solicitar al usuario los nombres personalizados
    screenshot_name = input("Ingresa el nombre para la captura de pantalla (deja vacío para usar la fecha y hora): ").strip() or None
    tasklist_name = input("Ingresa el nombre para el archivo de la lista de procesos (deja vacío para usar la fecha y hora): ").strip() or None

    captura_pantalla(screenshot_name)
    registro_procesos(tasklist_name)

if __name__ == "__main__":
    main()