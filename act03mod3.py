import pandas as pd
df = pd.read_csv("ventas.csv")
print(df)
print(df.head())
print(df[[" Producto"," Precio"]])
df_filtrado = df [df[" Precio"]>50]
print(df_filtrado)
df_filtrado.to_csv("df_filtrado.csv", index=False)