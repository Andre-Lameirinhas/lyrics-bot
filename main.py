import discord
import logging
from lyrics_gateway import get_lyrics
from utils import parse_message, get_cutoff_points
from constants import DISCORD_BOT_TOKEN, BAD_INPUT, NO_SONG_FOUND, LYRICS_CREDIT, LOG_LEVEL, LOG_FORMAT

logging.basicConfig(
    level=LOG_LEVEL.upper(),
    format=LOG_FORMAT
)

client = discord.Client()

@client.event
async def on_ready():
    logging.info('I\'m ready to search lyrics!')

@client.event
async def on_message(message):

    if not message.content.startswith('!lyrics'):
        return

    song, artist = parse_message(message.content)

    if not song:
        logging.error(f'Bad input received. input={message.content}')
        await message.channel.send(BAD_INPUT)
        return

    lyrics = get_lyrics(song, artist)

    if not lyrics:
        logging.error(f'No song found. song={song}, artist={artist}')
        await message.channel.send(NO_SONG_FOUND.format(song))
        return

    response = f'**{lyrics.song_name}** by **{lyrics.artist}**\n\n{lyrics.content}\n\n\n*{LYRICS_CREDIT}*'
    cutoffs = get_cutoff_points(response)

    cutoffs_it = iter(cutoffs)
    await message.channel.send('>>> ' + next(cutoffs_it))

    for cutoff in cutoffs_it:
        await message.channel.send('|')
        await message.channel.send('>>> ' + cutoff)

    logging.info('Lyrics retrieved successfully!')

client.run(DISCORD_BOT_TOKEN)
