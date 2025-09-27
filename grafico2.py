import matplotlib.pyplot as plt
Meses = ["Enero", "Febrero", "Marzo"]
Ventas = [200,250,300]

plt.plot(Meses, Ventas, marker="o")
plt.title( "Evolucion de Ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()


