import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Lyrics.com
LYRICS_USER_ID = os.getenv('LYRICS_USER_ID')
LYRICS_TOKEN = os.getenv('LYRICS_TOKEN')
LYRICS_ENDPOINT = os.getenv('LYRICS_ENDPOINT')
LYRICS_CREDIT = 'powered by https://www.lyrics.com'

# Genius.com
GENIUS_CLIENT_ID = os.getenv('GENIUS_CLIENT_ID')
GENIUS_CLIENT_SECRET = os.getenv('GENIUS_CLIENT_SECRET')
GENIUS_CLIENT_ACCESS_TOKEN = os.getenv('GENIUS_CLIENT_ACCESS_TOKEN')
GENIUS_ENDPOINT = os.getenv('GENIUS_ENDPOINT')

# Discord
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DISCORD_MESSAGE_MAX_LENGTH = 2000

# Messages
BAD_INPUT = 'Something is wrong with your input. Usage: `!lyrics song` or `!lyrics song - artist`'
NO_SONG_FOUND = 'No song named \'{}\' was found. I\'m sorry...'

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL')
LOG_FORMAT = '%(asctime)s [%(levelname)s] (%(module)s) - %(message)s'
