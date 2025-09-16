colores=0;

#AGREGAR UN ELEMENTO
#anadir al final
colores.append("amarillo")
print(colores)

#insertar en una posicion especifica
colores.insert(1,"naranja")
print(colores)

#comprobar si un elemto esta en la lista
print("rojo" in colores)  #true or false

#ELIMINAR ELEMENTOS
#eliminar un elemento especifico
colores.remove("verde") 
print(colores)

#eliminar por indice
del colores[0]  
print(colores)

#vaciar la lista
colores.clear() 
print(colores)

#MODIFICAR UN ELEMENTO
colores[0]="morado"
print(colores)

#LONGITUD DE UNA LISTA
print(len(colores))

DeprecationWarning    









