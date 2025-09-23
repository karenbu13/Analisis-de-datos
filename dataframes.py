import pandas as pd

#Crear un dataframe desde un diccionario

datos = { 
    'nombre':[ 'Ana', 'Luis', "Carlos"],
    'Edad': [23, 34, 29],
    'Ciudad' : ['Bogota', 'Medellin', 'Cali']
}
df=pd.DataFrame(datos)
print(df)

#Dataframe a partir de un diccionario

d= {'nombre':['Juan', 'Carla', 'Judith'], 'edad': ['23', '28', '25'], 'peso': [70.5, 56.7, 52.20]}
df=pd.DataFrame(d)
print(d) 

#Dataframe a partir de lista de lista

lst=[['Juan', 23,70.5],['Carla',28,56.7],['Judith', 25, 51.2]]
df= pd.DataFrame(lst, columns=['nombre', 'edad', 'peso'],index= ['it1','it2', 'it3'])
print(df)

