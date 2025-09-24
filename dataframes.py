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

#dataframe a partir de un diccionario de Series

S1= pd.Series(['Juan', 'Carla', 'judith'], index= ['item1', 'item2', 'item3'])
S2= pd.Series([ 23, 28, 25], index= ['item1', 'item2', 'item3'])
S3= pd.Series([ 70.5, 56.7, 51.2], index= ['item1', 'item2', 'item3'])
d1 = { 'nombre': S1, 'edad': S2, 'peso': S3}
df1= pd.DataFrame(d1)
print(df1)

S4= pd.Series([1.84,1.65,1.69,1.78], index= ['item1', 'item2', 'item3', 'item4'])
d2={ 'nombre':S1, 'edad':S2, 'peso': S3, 'altura': S4}
df2=pd.DataFrame(d2)
print(df2)

d3={'nombre': S1, 'edad':S2, 'peso': S3, 'altura': S4}
df3=pd.DataFrame(d3)
print(df3)

#acceso mediante posiciones
print(df3.iloc[0, 0])
print(df3.iloc[1])

#acceso mediante nombres
print(df)
print(df.loc['it1', 'nombre'])
print(df.loc['it1'])

df['altura'] = [1.84, 1.65, 1.69]
print(df) # se anade la columna áltura

df['IMC'] = df['peso']/df [ 'altura'] **2
print(df)

df.name= 'Datos Clìnicos'
print(df.size)
print(df.shape)
print(df.columns)
print(df.index)
print(df.head(2))
print(df.dtypes)


