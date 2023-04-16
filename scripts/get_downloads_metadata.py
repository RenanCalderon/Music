from Music.Beatport import Beatport
from Music.Directorios import *
from files.parameters import parametros

import os
import shutil

# Iniciar instancia
meta = Beatport()
# Ruta
path = parametros["path"]["downloads"]
destino = parametros["path"]["landing_folder"]
# Obtener archivos Mp3 de la ruta
songs = get_songs_from_dir(path.format(""))

no_encontradas = []
for sg in songs:

    # Obetener metadata
    file = path.format(sg)
    info = meta.getSongMetadata(file=file)
    # print(info)
    if info != "Not Found":
        name_info = f"{info[1]} - {info[0]} ({info[2]}).mp3"

        print(f"Nombre del archivo: {sg}")
        print(f"Busqueda Beatport: {name_info}")

        match = input("""La busqueda es correcta?\n[x]: No\n[y]: Si\nIngresa un valor: """)

        if match != "y":
            no_encontradas.append(sg)
        else:
            if sg != name_info:
                # Modificar nombre archivo
                audio = path.format(name_info)
                os.rename(file, audio)
                update_metadata(audio, info)
                shutil.move(audio, destino)
            else:
                update_metadata(file, info)
                shutil.move(file, destino)
    else:
        no_encontradas.append(sg)

print(no_encontradas)