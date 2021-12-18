import requests
from bs4 import BeautifulSoup
from constants import LYRICS_ENDPOINT, LYRICS_USER_ID, LYRICS_TOKEN
from utils import Lyrics


def get_lyrics(song_name: str, artist_name: str = '') -> Lyrics:
    search_res = requests.get(
        url = LYRICS_ENDPOINT,
        params = {
            'uid': LYRICS_USER_ID,
            'tokenid': LYRICS_TOKEN,
            'term': song_name,
            'artist': artist_name,
            'format': 'json'
        }
    )

    song_results = search_res.json()

    if len(song_results) == 0:
        return

    song = song_results['result'][0]

    return Lyrics(
        song_name = song['song'],
        artist = song['artist'],
        content = _scrape_lyrics_from_page(song['song-link'])
    )

def _scrape_lyrics_from_page(song_url: str) -> list[str]:
    page = requests.get(song_url)
    html = BeautifulSoup(page.content, 'html.parser')
    lyrics_div = html.find('pre', id='lyric-body-text')

    return lyrics_div.text
