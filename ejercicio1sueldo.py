i=0;sueldo=0; empleados=0; nuevo_sueldo=0; total_nomina=0;sueldos=0;sueldo_empleado2=0;aumento=0;
empleados=int(input("por favor ingrese el numero de empleados"))

for i in range (empleados):
    sueldo = float(input(f"ingrese el sueldo del empleado {i+1}: "))
   
    if sueldo<1000000:
        aumento=sueldo*0.15
    if sueldo>=1000000:  
        aumento=sueldo*0.12

    sueldos_nuevos=sueldo+aumento   
    total_nomina+=sueldos_nuevos
    print(f"empleado {i+1} sueldo_nuevo:  ${sueldos_nuevos:})
          
print(f"el total de la nomina es: ${total_nomina:}")

#fin del programa

         
           


    
   