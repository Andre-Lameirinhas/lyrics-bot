import requests
from bs4 import BeautifulSoup
from constants import GENIUS_ENDPOINT, GENIUS_CLIENT_ACCESS_TOKEN
from utils import Lyrics


def get_lyrics(song_name: str) -> Lyrics:
    search_res = requests.get(
        url = GENIUS_ENDPOINT,
        params = { 'q': song_name },
        headers = { 'Authorization': 'Bearer ' + GENIUS_CLIENT_ACCESS_TOKEN }
    )

    song_hits = search_res.json()['response']['hits']

    if len(song_hits) == 0:
        print('No song found.')
        return Lyrics(found = False)

    song = song_hits[0]['result']

    print(f'lyrics state = {song["lyrics_state"]}')

    return Lyrics(
        song_name = song['title'],
        artist = song['artist_names'],
        content = _scrape_lyrics_from_page(song['url'])
    )

# currently broken
def _scrape_lyrics_from_page(song_url: str) -> list[str]:
    page = requests.get(song_url)

    html = BeautifulSoup(page.content, 'html.parser')

    lyrics_div = html.find('div', class_='lyrics')

    if lyrics_div is None:
        print('Got the bad URL, retrying...')
        return _scrape_lyrics_from_page(song_url)

        
    print('Got the lyrics!')
    return lyrics_div.text
