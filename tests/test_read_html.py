import bs4, requests, time
from Levenshtein import distance
from files.parametros_public import parametros


inicio = time.time()
#Variables
song = "Supermode - Tell Me Why (Meduza Extended Remix)"
similitud = len(song)
file = "search_song.html"
url_song = parametros["platforms"]["beatport"]["bp_url"]

with open(file, 'rb') as f:
    soup = bs4.BeautifulSoup(f.read().decode("utf-8"), "lxml")
# search tracks
tracks = soup.select(".bucket-item.ec-item.track")

for track in tracks:
    name = track["data-ec-name"]
    artist = track["data-ec-d1"]
    add = track.find("span", class_="buk-track-remixed")
    song_b = f"{artist} - {name} ({add.string})"
    dist = distance(song, song_b)
    if dist < similitud:
        similitud = dist
        href = track.select_one("p.buk-track-title a")["href"]

# Poner alguna regla para capturar cuando no este en beatport y no ponga alguna

url_song = url_song.format(href)
resultado = requests.get(url_song)

with open('info_song.html', 'wb') as f:
    f.write(resultado.text.encode("utf-8"))

fin = time.time()
print(f"Execution time: {round(fin - inicio, 2)} segundos")