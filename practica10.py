import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Ejemplo de carga de datos (reemplázalo con tus propios datos)
# Asegúrate de tener una columna llamada 'Texto' que contenga el texto que quieres visualizar en la nube de palabras.
df = pd.read_csv('nba_modificado.csv')

# Concatenar el texto de todas las filas en una sola cadena
text = ' '.join(df['Nombre'].astype(str))

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(text)

# Visualizar la nube de palabras
plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()
