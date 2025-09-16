#creacion de un diccionario
mi_diccionario = {      
    "nombre": "Jhon",
    "edad": 30, 
    "ciudad": "New York"
}
print(mi_diccionario)

#acceso a valores mediante claves
print("nombre:", mi_diccionario["nombre"])
print("edad:", mi_diccionario["edad"])
print("ciudad:", mi_diccionario["ciudad"]) 

#modificacion de valores
mi_diccionario["edad"] = 26 
print("edad actualizada:", mi_diccionario["edad"])

#agregar un nuevo par clave-valor   
mi_diccionario["profesion"] = "programador"
print("diccionario actualizado:", mi_diccionario)

#eliminar un elemento
del mi_diccionario["ciudad"]
print("diccionario despues de eliminar ciudad:", mi_diccionario)

#mostrar el diccionario completo
print("diccionario completo:", mi_diccionario)











