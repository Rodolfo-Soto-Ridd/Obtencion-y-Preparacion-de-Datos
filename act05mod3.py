import pandas as pd
import numpy as np
import statistics as st
datos = [
    { "Estudiante":"Juan", "Materia":"Matemáticas", "Calificación":6.5},
    { "Estudiante":"Juan", "Materia":"Historia", "Calificación":5.8},
    { "Estudiante":"María", "Materia":"Matemáticas", "Calificación":4.2},
    { "Estudiante":"María", "Materia":"Historia", "Calificación":6.0},
]
print(datos)
df = pd.DataFrame(datos)
print(df)
df.set_index(["Estudiante","Materia"], inplace=True)
print(df)
print(df.loc[("María","Historia"),:])
df_group = df.groupby("Materia")["Calificación"].agg(["mean","max"])
print(df_group)
df_pivot = df.pivot_table(values="Calificación", index="Estudiante" ,columns="Materia")
print(df_pivot)
df_pivot=df_pivot.reset_index()
df_melted = pd.melt(df_pivot, id_vars="Estudiante", var_name="Materia",value_name="Calificación")
print(df_melted)
datos1 = {
    "ID_Estudiante": [125,233,222],
    "Estudiante": ["Carlos", "Lina", "Juana"],
    "Carrera": ["Matemática","Eléctrica","Educación"]
}
datos2 = {
    "ID_Estudiante": [131,222,301,47],
    "Materia": ["Calculo", "Algebra", "Programación", "Tecnología"],
    "Calificación": [6.3,5.2,5.8,6.7]
}
df1 = pd.DataFrame(datos1)
df2 = pd.DataFrame(datos2)
df_concat = pd.concat([df1,df2], axis = 1)
print(df_concat)
df_merged = pd.merge(
    df1,
    df2,
    on="ID_Estudiante",
    suffixes=("_df1","_df2")
)
print(df_merged)