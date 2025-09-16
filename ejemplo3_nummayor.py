

numero1=0;numero2=0;numero3=0;
numero1=int(input("por favor ingrese el primer numero"))
numero2=int(input("por favor ingrese el segundo numero"))
numero3=int(input("por favor ingrese el tercer numero"))

if(numero1>numero2) and (numero1>numero3):
    mayor=numero1
elif(numero2>numero1) and (numero2>numero3):
    mayor=numero2
else:
    mayor=numero3

print("el numero mayor es", mayor)

            
            