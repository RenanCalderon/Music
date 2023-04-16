import logging

from Music.Beatport import Beatport
from files.parameters import parametros

LOGGER = logging.getLogger()
LOGGER.setLevel('INFO')


def test_get_beatport_playlist():

    beatport = Beatport()
    playlist_num = parametros["platforms"]["beatport"]["playlist_example"]

    response = beatport.get_beatport_playlist(playlist_num)

    LOGGER.info(response)
    assert response
