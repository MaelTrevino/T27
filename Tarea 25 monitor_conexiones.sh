#!/bin/bash

# Monitorear conexiones de red activas y mostrar la salida en la terminal.
netstat -tunapl | grep ESTABLISHED

# Verificar si hubo algún error con la ejecución de netstat
if [ $? -ne 0 ]; then
    echo "Error al ejecutar el comando netstat."
    exit 1
fi