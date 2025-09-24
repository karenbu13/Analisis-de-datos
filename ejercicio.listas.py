# lista vacia
mi_lista= []

#lista con elementos
colores = ["rojo", "azul", "verde"]

#lista con diferentes tipos de datos
mixta=[1,"hola", 3.5, True]

import panda as pd
datos = {
    'valores':[100,200,300,400,500],
    'semana': ['Lunes', 'Martes', 'Miercoles', 'Jueves','Viernes']
}
df=pd.DataFrame(datos)
print(df)


