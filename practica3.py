import pandas as pd
from scipy import stats

# Lee el archivo CSV
archivo_csv = "nba_modificado.csv"  # Reemplaza con el nombre de tu archivo CSV
df = pd.read_csv(archivo_csv)

# Convierte las columnas en valores numéricos y maneja valores faltantes
df = df.apply(pd.to_numeric, errors='coerce').fillna(0)

# Calcula las estadísticas deseadas
minimo = df.min()
maximo = df.max()
conteo = df.count()
sumatoria = df.sum()
media = df.mean()
varianza = df.var()
desviacion_estandar = df.std()
asimetria = df.skew()
kurtoxis = df.kurtosis()

# Imprime las estadísticas
print("Mínimo:")
print(minimo)
print("\nMáximo:")
print(maximo)
print("\nConteo:")
print(conteo)
print("\nSumatoria:")
print(sumatoria)
print("\nMedia:")
print(media)
print("\nVarianza:")
print(varianza)
print("\nDesviación Estándar:")
print(desviacion_estandar)
print("\nAsimetría:")
print(asimetria)
print("\nKurtosis:")
print(kurtoxis)