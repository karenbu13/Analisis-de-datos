i=0;suma=0;sueldo=0;promedio=0;mayor=0;menor=0
while i<5:

    sueldo=float(input("por favor ingrese el sueldo"))
    if(i==0):
        mayor=sueldo
        menor=sueldo
    suma=suma+sueldo

    if (sueldo > mayor):
        mayor=sueldo
    if (sueldo<menor):
        menor=sueldo
    i=i+1
promedio=suma/5

print("el total de la nomina es:", suma)
print("el promedio de los sueldos es:", promedio)
print("el sueldo mayor es:", mayor)
print("el sueldo menor es:",menor)



