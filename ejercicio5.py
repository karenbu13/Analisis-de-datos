mi_lista=[1,2,3,4,5]
for elemento in mi_lista:
    print(elemento)

mi_tupla = ('a','b','c', 'd') 
for elemento in mi_tupla:
    print(elemento)

mi_diccionario = {'nombre': 'juan', 'edad': 30, 'ciudad': 'ejemplo'}
for clave in mi_diccionario:
    print(clave) 

mi_diccionario = {'nombre': 'juan', 'edad': 30, 'ciudad': 'ejemplo'}
for clave, valor in mi_diccionario.items():
  print(clave,":" ,valor) 

mi_cadena="Python"
for caracter in mi_cadena:
    print(caracter)  

numeros= [2,4,6,8,10]   
suma=0
for num in numeros:
    suma += num
    print("la suma de los numeros en la lista es:", suma)

