import bs4
import time


inicio = time.time()
file = "info_song.html"

with open(file, 'rb') as f:
    soup = bs4.BeautifulSoup(f.read().decode("utf-8"), "lxml")

info = soup.select(".interior-track-content-item")
info_list = []
for item in info:
    info_list.append(item.select("span", class_="value"
                                 )[1].text.replace("\n", ""))

fin = time.time()
print(f"Execution time: {round(fin - inicio, 2)} segundos")

print(info_list)
