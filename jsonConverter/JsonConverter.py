import os
import json

def obtener_estructura_directorio(path):
    estructura = {
        "ruta": path.replace("\\", "/"),
        "carpetas": []
    }

    # Solo buscamos carpetas en este caso
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            temporada = {
                "NumeroTemporada": item,
                "archivos": []
            }
            archivos_temporada = os.listdir(item_path)
            # Agregamos los archivos de la temporada
            for archivo in archivos_temporada:
                if os.path.isdir(os.path.join(item_path, archivo)):
                    miniatura = {
                        "Miniaturas": archivo,
                        "archivos": os.listdir(os.path.join(item_path, archivo))
                    }
                    temporada["archivos"].append(miniatura)
                else:
                    temporada["archivos"].append(archivo)
            estructura["carpetas"].append(temporada)

    return estructura

# Rutas de ejemplo, ajusta según tus directorios
directorios = [
    "z:/elbauldegegy/multimedia/series/DragonBallGT/"
]

for directorio in directorios:
    estructura_json = obtener_estructura_directorio(directorio)

    # Serializar la estructura en formato JSON
    json_output = json.dumps(estructura_json, indent=4)
    print(json_output)
    print("\n\n")
