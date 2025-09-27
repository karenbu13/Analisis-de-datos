import matplotlib.pyplot as plt

meses= ["Enero", "Febrero", "Marzo", "Abril"]
ventas= [1500,1800,1200,2000]

#grafico que muestre las ventas por cada mes

plt.bar(meses,ventas)
plt.title("Ventas por Cada Mes")
plt.xlabel("meses")
plt.ylabel("ventas")
plt.show()

#Grafico de lineas que muestre tendencia de las ventas

plt.plot(meses,ventas)
plt.title("Ventas por Cada Mes")
plt.xlabel("meses")
plt.ylabel("ventas")
plt.grid(True)
plt.show()

#Grafico de dispercion

plt.scatter(meses,ventas, color="blue")
plt.title("Relacion entre Gasto y Ventas")
plt.xlabel("Gasto Publicitario")
plt.ylabel("Ventas")
plt.show()
