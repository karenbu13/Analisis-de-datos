#Crear una serie con los siguientes datos:[100,200,300,400,500]
import pandas as pd
serie= pd.Series([100,200,300,400,500], index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'])
print(serie)
print(serie['Miercoles'])
print(serie.mean())
nueva_serie=serie+50
print(nueva_serie)

#crea un DataFrame

datos={
    'Producto': ['Manzana', 'Banana', 'Cereza'],
    'Precio': [2.5, 1.8, 3.0],
    'cantidad': [10, 15, 8]
}
df=pd.DataFrame(datos)
print(df)


   