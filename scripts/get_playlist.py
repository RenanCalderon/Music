from Music.Beatport import Beatport
from files.parameters import parametros

beatport = Beatport()
playlist_num = 1909357

response = beatport.get_beatport_playlist(playlist_num)

print(response)