import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn import utils
# Supongamos que tienes un DataFrame llamado df con características y etiquetas de clase.
# Asegúrate de tener una columna llamada 'Clase' que contiene las etiquetas de clase.

df = pd.read_csv('nba_modificado.csv')
df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
# Dividir los datos en conjuntos de entrenamiento y prueba
X = df.drop('Puntos', axis=1)  # Características
y = df['Puntos']  # Etiquetas de clase
lab = preprocessing.LabelEncoder()

y_transform = lab.fit_transform(y)



X_train, X_test, y_train, y_test = train_test_split(X, y_transform, test_size=0.2, random_state=42)

# Crear y entrenar el modelo k-NN
k = 3  # Puedes ajustar el valor de k según tus necesidades

modelo_knn = KNeighborsClassifier(n_neighbors=k)

modelo_knn.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = modelo_knn.predict(X_test)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

print('\nMatriz de Confusión:')
print(confusion_matrix(y_test, y_pred))

print('\nReporte de Clasificación:')
print(classification_report(y_test, y_pred))
