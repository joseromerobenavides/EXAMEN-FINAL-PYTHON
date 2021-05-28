import pandas as pd
import numpy as np

nombres = ['Juan', 'Laura', 'Pepe']
edades = [42, 40, 37]

df['Nombre'] = nombres
df['Edad'] = edades

nueva_fila = { 'Nombre': 'Paco', 'Edad': 29} # creamos un diccionario
df = df.append(nueva_fila, ignore_index=True)

nueva_fila = pd.Series(['Ana', 33], index=df.columns) # creamos un objeto Seris
df = df.append(nueva_fila, ignore_index=True)

print(df)

array = np.array([
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33]
])
columnas = ['C1', 'C2', 'C3', 'C4'] # esta lista también podría ser un array de NumPy

df = pd.DataFrame(array, columns = columnas)

print(df)

datos = [
    {'Nombre': 'Juan', 'Edad': 42, 'Departamento': 'Comunicación'},
    {'Nombre': 'Laura', 'Edad': 44, 'Departamento': 'Administración'},
    {'Nombre': 'Pepe', 'Edad': 37, 'Departamento': 'Ventas'}
]

df = pd.DataFrame(datos)

print(df)


datos = {
    'Nombre' : ['Juan', 'Laura', 'Pepe'],
    'Edad': [42, 40, 37],
    'Departamento': ['Comunicación', 'Administración', 'Ventas']
}

df = pd.DataFrame(datos)

print(df)