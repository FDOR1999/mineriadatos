import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('nba.csv')

# Lista de nombres de las columnas a eliminar
columnas_a_eliminar = ['net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct']

# Elimina las columnas
df = df.drop(columnas_a_eliminar, axis=1)

# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('nba_modificado.csv', index=False)
 
 #--------------------------------------------------------


# Lee el archivo CSV
df = pd.read_csv('nba_modificado.csv')

# Diccionario de mapeo para cambiar los nombres de las columnas
nombres_nuevos = {
   
'player_name': 'Nombre',
'team_abbreviation': 'Abreviacion_del_equipo',
'age': 'Edad',
'player_height': 'Altura_del_jugador',
'player_weight': 'Peso_del_jugador',
'college': 'Universidad',
'country': 'Pais',
'draft_year': 'Año_de_seleccion',
'draft_round': 'Ronda_de_seleccion',
'draft_number': 'Numero_de_seleccion',
'gp': 'Juegos_jugados',
'pts': 'Puntos',
'reb': 'Rebotes',
'ast': 'Asistencias',
'season': 'Temporada',

}

# Cambia los nombres de las columnas
df = df.rename(columns=nombres_nuevos)
df = df.drop('Unnamed: 0', axis=1)
# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('nba_modificado.csv', index=False)

