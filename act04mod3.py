import pandas as pd
df_ventas = pd.read_csv("ventas.csv")
print(df_ventas)
print(df_ventas.isnull())
print(df_ventas.isnull().sum())
df_ventas_clean = df_ventas.dropna()
df_ventas_s_duplicado = df_ventas_clean.drop_duplicates()
print(df_ventas_s_duplicado)
q1 = df_ventas_s_duplicado["Cantidad"].quantile(0.25)
q3 = df_ventas_s_duplicado["Cantidad"].quantile(0.75)
iqr = q3 - q1
df_ventas_s_duplicado_out = df_ventas_s_duplicado[(df_ventas_s_duplicado["Cantidad"]>= q1 - 1.5 * iqr) & (df_ventas_s_duplicado["Cantidad"]<= q3 - 1.5 * iqr)]
print(df_ventas_s_duplicado_out)