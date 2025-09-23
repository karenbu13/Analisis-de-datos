import datetime
ahora=datetime.datetime.now()
print(ahora)  #Salida: 2024-06-17 12:34:56 ejemplo   

print(ahora.strftime("%Y-%m-%d"))  #Salida: 2024-06-17

fecha1=datetime.datetime(2025,1,20)    
fecha2=datetime.datetime(2024,12,25)
diferencia=fecha1-fecha2    
print(diferencia.days)

fecha_str="2024-07-15"
fecha=datetime.datetime.strptime(fecha_str,"%Y-%m-%d")
print(fecha)  #Salida: 2024-07-15 00:00:00 

fechas=["2024-06-20","2024-07-01","2024-06-15"]
formateadas = [datetime.datetime.strptime(f,"%Y-%m-%d") for f in fechas]
meses = [f.strftime("%B") for f in formateadas]




