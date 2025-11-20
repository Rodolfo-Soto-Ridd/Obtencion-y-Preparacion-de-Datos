import numpy as np
import pandas as pd
# 1. Limpieza y Transformación de Datos (3 puntos). 
# Carga el dataset en un DataFrame de Pandas. 
# Identifica y trata valores perdidos en el dataset. 
# Detecta y filtra outliers usando el método del rango intercuartílico (IQR).  
# Reemplaza los valores de la columna "Razon_Migracion" usando mapeo de valores 
# (ejemplo: "Económica" → "Trabajo", "Conflicto" → "Guerra"). 
datos = pd.read_csv("migracion.csv")
df = pd.DataFrame(datos)
print(f"\n",df)
df.isnull()
df.dropna()
# Metodo clases "Cantidad Migrante"
q1=df["Cantidad_Migrantes"].quantile(0.25)
print(f"\nq1:",q1)
q3=df['Cantidad_Migrantes'].quantile(0.75)
print(f"\nq3:",q3)
iqr=q3-q1
print(f"\niqr:",iqr)
df_filtrado=df[(df['Cantidad_Migrantes']>=q1-1.5*iqr)&(df['Cantidad_Migrantes']<=q3+1.5*iqr)]
print(f"\nDataFrame Filtrado por Cantidad de Migrantes:\n",df_filtrado)

q1=df["PIB_Origen"].quantile(0.25)
print(f"\nq1:",q1)
q3=df['PIB_Origen'].quantile(0.75)
print(f"\nq3:",q3)
iqr=q3-q1
print(f"\niqr:",iqr)
df_filtrado=df[(df['PIB_Origen']>=q1-1.5*iqr)&(df['PIB_Origen']<=q3+1.5*iqr)]
print(f"\nDataFrame Filtrado por PIB de Origen:\n",df_filtrado)

q1=df["PIB_Destino"].quantile(0.25)
print(f"\nq1:",q1)
q3=df['PIB_Destino'].quantile(0.75)
print(f"\nq3:",q3)
iqr=q3-q1
print(f"\niqr:",iqr)
df_filtrado=df[(df['PIB_Destino']>=q1-1.5*iqr)&(df['PIB_Destino']<=q3+1.5*iqr)]
print(f"\nDataFrame Filtrado por PIB de Destino:\n",df_filtrado)

q1=df["IDH_Origen"].quantile(0.25)
print(f"\nq1:",q1)
q3=df['IDH_Origen'].quantile(0.75)
print(f"\nq3:",q3)
iqr=q3-q1
print(f"\niqr:",iqr)
df_filtrado=df[(df['IDH_Origen']>=q1-1.5*iqr)&(df['IDH_Origen']<=q3+1.5*iqr)]
print(f"\nDataFrame Filtrado por IDH de Origen:\n",df_filtrado)

q1=df["IDH_Destino"].quantile(0.25)
print(f"\nq1:",q1)
q3=df['IDH_Destino'].quantile(0.75)
print(f"\nq3:",q3)
iqr=q3-q1
print(f"\niqr:",iqr)
df_filtrado=df[(df['IDH_Destino']>=q1-1.5*iqr)&(df['IDH_Destino']<=q3+1.5*iqr)]
print(f"\nDataFrame Filtrado por IDH de Destino:\n",df_filtrado)


# Metodo "Cantidad Migrantes" como función
def filtrar_outlier_iqr(df,columnas):
    for col in columnas:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3-q1
        limite_inferior = q1-1.5*iqr
        limite_superior = q3+1.5*iqr
        df=df[(df[col]>=limite_inferior)&(df[col]<=limite_superior)]
    return df
columnas_numericas = ['Cantidad_Migrantes','PIB_Origen','PIB_Destino','IDH_Origen','IDH_Destino']
df=filtrar_outlier_iqr(df,columnas_numericas)
print(f"\nDataFrame Filtrado\n",df)

mapeo_razones = {'Económica':'Trabajo',
                 'Conflicto':'Guerra',
                 'Educativa':'Estudios'}

df['Razon_Migracion']=df['Razon_Migracion'].map(mapeo_razones).fillna(df['Razon_Migracion'])
print(f"\nDataset Limpio y Transformado:")
print(df)

# 2. Análisis Exploratorio (2 puntos) 
# Muestra las 5 primeras filas del dataset. 
# Obtén información general del dataset con .info() y .describe(). 
# Calcula estadísticas clave: 
# Media y mediana de la cantidad de migrantes. 
# PIB promedio de los países de origen y destino: Usa .value_counts() para contar cuántos movimientos de migración ocurrieron 
# por cada razón.  

print(f"\n",df.head(5))
print(f"\n",df.info())
print(f"\n",df.describe())
print(f"\nEl Promedio de la Cantidad de Migrantes es: ",df['Cantidad_Migrantes'].mean())
print(f"\nLa Mediana de la Cantidad de Migrantes es: ",df['Cantidad_Migrantes'].median())
print(f"\nEl Promedio del PIB de Origen es: ",df['PIB_Origen'].mean())
print(f"\nEl Promedio del PIB de Destino es: ",df['PIB_Destino'].mean())
print(f"\nLas Cantidades Totales por Razon de Migración son:\n",df['Razon_Migracion'].value_counts())

# 3. Agrupamiento y Sumarización de Datos (2 puntos) 
# • Agrupa los datos por "Razon_Migracion" y calcula la suma total de migrantes para cada categoría. 
# • Obtén la media del IDH de los países de origen por cada tipo de migración. 
# • Ordena el DataFrame de mayor a menor cantidad de migrantes.

df_grouped_sum = df.groupby('Razon_Migracion')['Cantidad_Migrantes'].sum()
print(f"\nLa Cantidad Total de Migrantes por Razón de Migración es de:\n",df_grouped_sum)
df_grouped_mean = df.groupby(by=['Razon_Migracion'])['IDH_Origen'].mean()
print(f"\nEl Promedio de IDH de origen por Tipo de Migración es de:\n",df_grouped_mean)
df_ordenado = df.sort_values(by=['Cantidad_Migrantes'], ascending=False)
print(f"\nA continuación se presenta el DataFrame ordenado de mayor a menor por cantidad de migrantes:\n",df_ordenado)

# 4. Filtros y Selección de Datos (2 puntos)
# • Filtra y muestra solo las migraciones por conflicto.
# • Selecciona y muestra las filas donde el IDH del país de destino sea mayor a 0.90.
# • Crea una nueva columna "Diferencia_IDH" que calcule la diferencia de IDH entre país de origen y destino.

nuevo_mapeo = {'Guerra':'Conflicto'}
df['Razon_Migracion']=df['Razon_Migracion'].map(nuevo_mapeo).fillna(df['Razon_Migracion'])
print("\n",df)
df_conflicto = df[df['Razon_Migracion']=='Conflicto']
print(f"\nLas migraciones por conflicto son:\n",df_conflicto)
df_IHD_Destino = df[df['IDH_Destino']>0.9]
print(f"\nLos paises con IDH de Destino superior a 0,9 son:\n",df_IHD_Destino)
df["Diferencia_IDH"]=df['PIB_Destino']-df['IDH_Origen']
print(f"\nLos datos con las nueva columna 'Diferencia de IDH' se presentan a continuación:\n",df)

#5. Exportación de Datos (1 punto)
# • Guarda el DataFrame final en un nuevo archivo CSV llamado "Migracion_Limpio.csv", sin el índice.

df.to_csv('Migracion_limpio.csv', index = False)