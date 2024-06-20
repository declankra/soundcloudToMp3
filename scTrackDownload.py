# 1. get track url from soundcloud (go to track's page) -> paste url
# 2. file will be saved in track_downloads folder in current directory
# 2. click file -> opens in itunes -> enjoy! 

## ! pip3 install soundcloud-lib
import asyncio
import os
from sclib.asyncio import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()  

async def get_track():
    track = await api.resolve('https://soundcloud.com/casso-wav/prada') # !! paste song url
    assert type(track) is Track
    return track


async def write_track_to_file(track, filename):
    if not os.path.exists('./track_downloads'): # creates 'track_downloads' directory if it doesn't exist
        os.makedirs('./track_downloads')
    with open(filename, 'wb+') as file:
        await track.write_mp3_to(file)

track = asyncio.run(get_track())
filename = f'./track_downloads/{track.artist} - {track.title}.mp3'
asyncio.run(write_track_to_file(track, filename)) # file will be saved in 'track_downloads' folder in currect directory


