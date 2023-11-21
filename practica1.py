import requests

# URL del archivo CSV que deseas descargar
url = "https://raw.githubusercontent.com/dxmedicalsolutions/sport-datasets-MBA-NFL-SOCCER-NFL-PGA-/main/nba.csv"

# Nombre de archivo local para guardar el archivo descargado
nombre_archivo_local = "nba.csv"

# Realiza la solicitud GET para descargar el archivo
respuesta = requests.get(url)

# Verifica si la descarga fue exitosa (código de respuesta 200)
if respuesta.status_code == 200:
    # Abre el archivo local en modo binario y escribe los datos descargados
    with open(nombre_archivo_local, 'wb') as archivo_local:
        archivo_local.write(respuesta.content)
    print("Descarga exitosa")
else:
    print("Error al descargar el archivo:", respuesta.status_code)