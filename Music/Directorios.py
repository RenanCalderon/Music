import os
from mutagen.id3 import ID3, TIT2, TPE2, TIT3, TCON, TBPM, TPUB, TKEY


def get_songs_from_dir(path):

    songs = []
    for archivo in os.listdir(path):
        if archivo.endswith(".mp3"):
            songs.append(archivo)
    return songs


def update_metadata(file, info):

    audio = ID3(file)

    # Name
    audio["TIT2"] = TIT2(encoding=3, text=[info[0]])
    # Artist
    audio["TPE2"] = TPE2(encoding=3, text=[info[1]])
    # Subtitulo
    audio["TIT3"] = TIT3(encoding=3, text=[info[2]])
    # Genero
    audio["TCON"] = TCON(encoding=3, text=[info[7]])
    # BPM
    audio["TBPM"] = TBPM(encoding=3, text=[info[5]])
    # Disquera
    audio["TPUB"] = TPUB(encoding=3, text=[info[8]])
    # Clave
    audio["TKEY"] = TKEY(encoding=3, text=[info[6]])

    audio.save()
