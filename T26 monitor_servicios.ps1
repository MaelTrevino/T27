#monitor_servicios.ps1
#Este script se encargara de monitorear los servicios del sistemas y exportara esta informacion a CSV

Get-Service | Select-Object Name, DisplayName, Status, StartType | 
    ConvertTo-Csv -NoTypeInformation