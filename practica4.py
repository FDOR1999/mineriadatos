import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV

df = pd.read_csv('nba_modificado.csv')

# Configuración de estilo de seaborn
sns.set(style="whitegrid")

# Convierte las columnas en valores numéricos y maneja valores faltantes
df = df.apply(pd.to_numeric, errors='coerce').fillna(0)



# Gráficos
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))

# Mínimo
sns.boxplot(x=df['Puntos'], ax=axs[0, 0])
axs[0, 0].set_title('Mínimo')

# Máximo
sns.boxplot(x=df['Puntos'], ax=axs[0, 1])
axs[0, 1].set_title('Máximo')

# Conteo
sns.histplot(df['Puntos'], ax=axs[0, 2], kde=False)
axs[0, 2].set_title('Conteo')

# Sumatoria
sns.lineplot(x=df.index, y=np.cumsum(df['Puntos']), ax=axs[1, 0])
axs[1, 0].set_title('Sumatoria')

# Media
sns.lineplot(x=df.index, y=np.cumsum(df['Puntos']) / np.arange(1, len(df) + 1), ax=axs[1, 1])
axs[1, 1].set_title('Media')

# Varianza
sns.lineplot(x=df.index, y=np.cumsum((df['Puntos'] - df['Puntos'].mean())**2) / np.arange(1, len(df) + 1), ax=axs[1, 2])
axs[1, 2].set_title('Varianza')

# Desviación estándar
sns.lineplot(x=df.index, y=np.sqrt(np.cumsum((df['Puntos'] - df['Puntos'].mean())**2) / np.arange(1, len(df) + 1)), ax=axs[2, 0])
axs[2, 0].set_title('Desviación Estándar')

# Asimetría
sns.histplot(df['Puntos'], ax=axs[2, 1], kde=True)
axs[2, 1].set_title('Asimetría')

# Kurtosis
sns.histplot(df['Puntos'], ax=axs[2, 2], kde=True)
axs[2, 2].set_title('Kurtosis')

# Gráficos
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))

# Mínimo
sns.boxplot(x=df['Rebotes'], ax=axs[0, 0])
axs[0, 0].set_title('Mínimo')

# Máximo
sns.boxplot(x=df['Rebotes'], ax=axs[0, 1])
axs[0, 1].set_title('Máximo')

# Conteo
sns.histplot(df['Rebotes'], ax=axs[0, 2], kde=False)
axs[0, 2].set_title('Conteo')

# Sumatoria
sns.lineplot(x=df.index, y=np.cumsum(df['Rebotes']), ax=axs[1, 0])
axs[1, 0].set_title('Sumatoria')

# Media
sns.lineplot(x=df.index, y=np.cumsum(df['Rebotes']) / np.arange(1, len(df) + 1), ax=axs[1, 1])
axs[1, 1].set_title('Media')

# Varianza
sns.lineplot(x=df.index, y=np.cumsum((df['Rebotes'] - df['Rebotes'].mean())**2) / np.arange(1, len(df) + 1), ax=axs[1, 2])
axs[1, 2].set_title('Varianza')

# Desviación estándar
sns.lineplot(x=df.index, y=np.sqrt(np.cumsum((df['Rebotes'] - df['Rebotes'].mean())**2) / np.arange(1, len(df) + 1)), ax=axs[2, 0])
axs[2, 0].set_title('Desviación Estándar')

# Asimetría
sns.histplot(df['Rebotes'], ax=axs[2, 1], kde=True)
axs[2, 1].set_title('Asimetría')

# Kurtosis
sns.histplot(df['Rebotes'], ax=axs[2, 2], kde=True)
axs[2, 2].set_title('Kurtosis')

# Gráficos
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))

sns.boxplot(x=df['Asistencias'], ax=axs[0, 0])
axs[0, 0].set_title('Mínimo')

# Máximo
sns.boxplot(x=df['Asistencias'], ax=axs[0, 1])
axs[0, 1].set_title('Máximo')

# Conteo
sns.histplot(df['Asistencias'], ax=axs[0, 2], kde=False)
axs[0, 2].set_title('Conteo')

# Sumatoria
sns.lineplot(x=df.index, y=np.cumsum(df['Asistencias']), ax=axs[1, 0])
axs[1, 0].set_title('Sumatoria')

# Media
sns.lineplot(x=df.index, y=np.cumsum(df['Asistencias']) / np.arange(1, len(df) + 1), ax=axs[1, 1])
axs[1, 1].set_title('Media')

# Varianza
sns.lineplot(x=df.index, y=np.cumsum((df['Asistencias'] - df['Asistencias'].mean())**2) / np.arange(1, len(df) + 1), ax=axs[1, 2])
axs[1, 2].set_title('Varianza')

# Desviación estándar
sns.lineplot(x=df.index, y=np.sqrt(np.cumsum((df['Asistencias'] - df['Asistencias'].mean())**2) / np.arange(1, len(df) + 1)), ax=axs[2, 0])
axs[2, 0].set_title('Desviación Estándar')

# Asimetría
sns.histplot(df['Asistencias'], ax=axs[2, 1], kde=True)
axs[2, 1].set_title('Asimetría')

# Kurtosis
sns.histplot(df['Asistencias'], ax=axs[2, 2], kde=True)
axs[2, 2].set_title('Kurtosis')


# Gráficos
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))

sns.boxplot(x=df['Juegos_jugados'], ax=axs[0, 0])
axs[0, 0].set_title('Mínimo')

# Máximo
sns.boxplot(x=df['Juegos_jugados'], ax=axs[0, 1])
axs[0, 1].set_title('Máximo')

# Conteo
sns.histplot(df['Juegos_jugados'], ax=axs[0, 2], kde=False)
axs[0, 2].set_title('Conteo')

# Sumatoria
sns.lineplot(x=df.index, y=np.cumsum(df['Juegos_jugados']), ax=axs[1, 0])
axs[1, 0].set_title('Sumatoria')

# Media
sns.lineplot(x=df.index, y=np.cumsum(df['Juegos_jugados']) / np.arange(1, len(df) + 1), ax=axs[1, 1])
axs[1, 1].set_title('Media')

# Varianza
sns.lineplot(x=df.index, y=np.cumsum((df['Juegos_jugados'] - df['Juegos_jugados'].mean())**2) / np.arange(1, len(df) + 1), ax=axs[1, 2])
axs[1, 2].set_title('Varianza')

# Desviación estándar
sns.lineplot(x=df.index, y=np.sqrt(np.cumsum((df['Juegos_jugados'] - df['Juegos_jugados'].mean())**2) / np.arange(1, len(df) + 1)), ax=axs[2, 0])
axs[2, 0].set_title('Desviación Estándar')

# Asimetría
sns.histplot(df['Juegos_jugados'], ax=axs[2, 1], kde=True)
axs[2, 1].set_title('Asimetría')

# Kurtosis
sns.histplot(df['Juegos_jugados'], ax=axs[2, 2], kde=True)
axs[2, 2].set_title('Kurtosis')









plt.tight_layout()
plt.show()
