import pandas as pd

datos = {
    'nombre':['manzanas', "peras", "Bananas", "Naranjas"],
    'Precio':[2.5 , 3.0 , 1.8 , 2.2 ],
    'Cantidad_Vendida':[100,150, 200, 80],
    'Mes': ["Enero", "Enero", "Febrero", "Febrero"]
}
df=pd.DataFrame(datos)
print(df)

filtro=df[df["Mes"]=="Enero"]
print(filtro)
print(df.loc[:,"nombre":"Cantidad_Vendida"])
df["Precio"] = df ["Precio"]+df["Precio"]* 0.1
print(df)
df["ingresos"]=df["Precio"]*df["Cantidad_Vendida"]
print(df)

