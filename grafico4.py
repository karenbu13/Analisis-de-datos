import matplotlib.pyplot as plt

Ingresos=[100,200,300,400,500]
gasto=[20,40,60,80,100]

plt.scatter(gasto,Ingresos, color="green")
plt.title("Relacion entre Gasto e Ingresos")
plt.xlabel("Gasto Publicitario")
plt.ylabel("Ingreso")
plt.show()