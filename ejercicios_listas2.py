#encontrar el numero mayor en una lista
numeros = [10, 5, 8, 20, 3]
mayor = numeros[0]  
for num in numeros:
    if num > mayor:
        mayor = num 
print("El numero mayor es:", mayor) 

