import pandas as pd

serie = pd.Series([10, 20, 30 , 40])
print(serie)

#personalizar el indice
serie = pd.Series([10,20,30,40], index=['A', 'B', 'C', 'D'])
print(serie) 
#operaciones con indices
print(serie["A"])  # accede a un valor especifico : salida 10
print(serie.mean())  #calcular el promedio: Salida : 25.0

#series a partir de diccionarios
dicc= {'mangos': 20,'naranjas': 33, 'fresas':52, 'peras': 20}
s= pd.Series(dicc)
print(s)

#etiqueta en indice que no esta en el diccionario, tendra valor que se representa x NaN
S= pd.Series(dicc,index=['mangos', 'naranjas', 'fresas', 'peras', 'kiwis'])
print(S)

# Indexacion o accesos a los elementos de la serie.
print (S['mangos'])
20.0
print (S[['mangos', 'fresas']]) #empaquetados en una lista

# Se pueden acceder tambien por su posicion 
print(S[0])
20.0
print(S[1:3])
print(S[2:])

# Metodos de la serie, ignoran valores NaN

S.name= 'Frutas de la compra'







