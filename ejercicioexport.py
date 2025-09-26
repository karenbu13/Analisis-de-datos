import pandas as pd
#df=pd.read_csv("C:/Users/Usuario/Desktop/Data Analysis/Registro_de_Ventas.csv")
#print(df)
#df=pd.read_csv("Registro_de_Ventas.csv", sep=";")
#df.to_excel("Ventas1.xlsx", index=False)
#df=pd.read_csv("Registro_de_Ventas.csv)
df=pd.read_excel("ventas1.xlsx", usecols="A:B")
print(df)

