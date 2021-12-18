from constants import DISCORD_MESSAGE_MAX_LENGTH
from dataclasses import dataclass
import re

@dataclass
class Lyrics:
    song_name: str = ''
    artist: str = ''
    content: str = ''

def get_cutoff_points(lyrics: str) -> list[str]:

    if len(lyrics) < DISCORD_MESSAGE_MAX_LENGTH - 4:
        return [lyrics]

    lyrics_lines = lyrics.split('\n')
    cutoffs = []
    cutoff = ''
    for line in lyrics_lines:
        if len(cutoff + line + '\n') > DISCORD_MESSAGE_MAX_LENGTH - 4:
            cutoffs.append(cutoff)
            cutoff = line + '\n'
        else:
            cutoff += line + '\n'
    cutoffs.append(cutoff)
    return cutoffs

def parse_message(message: str) -> tuple[str, str]:
    song = ''
    artist = ''

    if matched := re.fullmatch(r'!lyrics ([\w\' ]+)(-(.+))?', message):
        song = str(matched.group(1)).strip()
        if matched.group(3):
            artist = str(matched.group(3)).strip()

    return (song, artist)
