import requests
import bs4
from files.parametros_public import parametros

bp_search = parametros["platforms"]["beatport"]["bp_search"]
search = input("Input the song: ").replace(" ", "+")
page = bp_search.format(search)

resultado = requests.get(bp_search)
print(resultado.status_code)

soup = bs4.BeautifulSoup(resultado.content, "lxml")
print(soup)

# with open(f"search_{search}.html", 'wb') as f:
#     f.write(resultado.text.encode("utf-8"))