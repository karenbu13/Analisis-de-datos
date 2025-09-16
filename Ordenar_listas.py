#ordenar una lista   
numeros=[4,2,8,1,5]
numeros.sort()  #ordena la lista de menor a mayor # [1,2,4,5,8] 
print(numeros)
numeros.sort(reverse=True) #ordena la lista de mayor a menor #[8,5,4,2,1]   
print(numeros)

#concatenar listas
lista1=[1,2,3]  
lista2=[4,5,6]
lista_combinada=lista1+lista2
print(lista_combinada)

#iterar sobre una lista

colores=["rojo", "azul", "verde"]
#recorrer y mostrar cada elemento   
for color in colores:
    print(color)

#repetir un elemento varias veces
repetidos=["hola"]*3  #['hola', 'hola', 'hola']
print(repetidos)

repetidos=[5]*3    
print(repetidos)

print([0] * 5)  #[0, 0, 0, 0, 0]



 