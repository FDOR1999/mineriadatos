import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Ejemplo de carga de datos (reemplázalo con tus propios datos)
# Asegúrate de tener columnas relevantes para la agrupación.
df = pd.read_csv('nba_modificado.csv')
df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
# Seleccionar características relevantes
features = df[[
    'Puntos','Asistencias','Rebotes'
]]

# Escalar características para que tengan una escala similar
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Determinar el número de clusters (ajusta según tus necesidades)
k = 3

# Aplicar k-Means
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(features_scaled)

# Visualizar los resultados (puedes ajustar según el número de características)
plt.scatter(features_scaled[:, 0], features_scaled[:, 1], c=df['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, marker='X', c='red')
plt.title('Agrupación de Datos con k-Means')
plt.xlabel('Caracteristica1 (escalada)')
plt.ylabel('Caracteristica2 (escalada)')
plt.show()
