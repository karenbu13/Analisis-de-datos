import pandas as pd
#cargar un archivo CSV
#df=pd.read_csv("airports.csv")
#df=pd.read_csv("C:/Users/Usuario/Desktop/Data Analysis/airports.csv" )
#df=pd.read_csv("airports.csv",usecols=["id", "name","elevation_ft" ,"iso_country"])
#df=pd.read_csv("airports.csv",nrows=15)
#df=pd.read_excel("airports1.xlsx")
#print(df.head())
#df=pd.read_excel("airports1.xlsx", sheet_name="Hoja1")
#df=pd.read_excel("airports1.xlsx", usecols="A:C")
#df=pd.read_excel("airports1.xlsx", skiprows=2)
df=pd.read_excel("airports1.xlsx", nrows=10)
print(df)
#df.to_csv("exports.csv", index=False)
#df.to_csv("exports.csv", sep=";")
df.to_excel("exports2.xlsx", index=False)
 




